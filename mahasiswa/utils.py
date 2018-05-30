from datetime import datetime

from django.core.paginator import Paginator, EmptyPage

from api.db.utils import caching, create_mahasiswa_siak, convert_kode_to_nama
from api.ml_models import get_prediction, huruf_converter
from api.models import MahasiswaSIAK, PrediksiMataKuliah
from api.siak import get_jenjang, get_all_sks_term, \
    get_all_ip_term, get_sks_sequential, get_data_user, \
    get_total_mutu
from api.siak import get_nilai_prasyarat
from api.utils import give_verdict, save_status
from api.utils import save_status_matakuliah


def get_term(now):
    year = now.year
    term = 1
    if now.month < 8:
        year = now.year - 1
        term = 3
        if now.month > 2 and now.month < 7:
            term = 2
    term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
    return term_str


def get_context_mahasiswa(request, term_str):
    try:
        token = request.session['access_token']
        npm = request.session['kode_identitas']
        semester = get_semester_now(npm, int(term_str[-1:]))
        if request.session['kode_identitas'] != 'admin':
            mahasiswa, err = caching("get_data_user", get_data_user,
                                     (token, npm), npm)
            if err is None:
                request.session['name'] = mahasiswa['nama'].lower().title()
        else:
            request.session['name'] = 'admin'
        context = {
            'term': term_str,
            'team': 'usagi studio',
            'user': request.session['user_login'],
            'id': npm,
            'role': request.session['role'],
            'name': request.session['name'],
            'semester_now': str(semester)
        }
        return context

    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_recommendation(npm):
    print (npm)
    if MahasiswaSIAK.objects.filter(npm=npm).count() < 1:
        create_mahasiswa_siak(npm)
    mahasiswa = MahasiswaSIAK.objects.get(npm=npm)
    quer = PrediksiMataKuliah.objects.filter(npm=mahasiswa, status='lulus').order_by('kode_matkul')
    print(MahasiswaSIAK.objects.filter(npm=npm).count())
    res = []
    for prediksi in quer:
        nama_matkul = convert_kode_to_nama(prediksi.kode_matkul)
        res.append([prediksi.kode_matkul, nama_matkul])
    return res


def get_evaluation_status(term, sks_lulus, sks_diambil, ip_now=3.0, npm=""):
    if term % 2 > 0:
        term = term + 1  # evaluasi dilakukan di semester genap,jdi sks min nya disesuaikan
    sks_minimal = 12 * term  # still a temporary form , will be integrated with proper flow later
    verdict = caching("give_verdict", give_verdict,
                      (sks_minimal, sks_lulus, sks_diambil, ip_now), npm)
    return verdict


def request_evaluation_status(npm, token, term, sks_lulus=-1, mode=1):
    if sks_lulus < 0:
        if mode == 1:
            sks_lulus = caching("get_sks_sequential",
                                get_sks_sequential, (token, npm), npm)[0]
        else:
            pass
            # sks_lulus = caching("sks_lulus", get_sks, (token, npm), npm)[0]
    sks_diambil = 18
    ip_now = 3.0  # diitung ntr
    try:
        status = caching("get_evaluation_status", get_evaluation_status,
                         (term, sks_lulus, sks_diambil, ip_now, npm), npm)
        save_status(npm, status)
        return status
    except TypeError:
        return "Argument salah"


def request_course_prediction(npm, mk_target, nilai):
    print(nilai)
    status = get_prediction(prass=nilai, nama_matkul=mk_target)
    save_status_matakuliah(npm, mk_target, status)
    return status


# def get_query_checker(request, query_matkul, context):
#     pass


def get_prediktor_matkul_context(request, matkul_to_predict, context):
    try:
        token = request.session['access_token']
    except AttributeError as ex:
        return str(ex)
    except KeyError as ex:
        return str(ex)
    context_prediktor_matkul = {}
    prasyarat = get_nilai_prasyarat(token, context['id'], matkul_to_predict)
    nilai_prasyarat = prasyarat[0]
    scores = []
    not_found = 'Mata Kuliah atau Prasyarat Tidak Ditemukan'
    print("matkul_to_predict", matkul_to_predict, nilai_prasyarat)
    if isinstance(nilai_prasyarat, str) and nilai_prasyarat == not_found:
        status_matkul = not_found
    else:
        for key in nilai_prasyarat:
            if nilai_prasyarat[key] == '-':
                continue
            scores.append(huruf_converter(nilai_prasyarat[key]))
        status_matkul = request_course_prediction(context['id'], matkul_to_predict, scores)
    context_prediktor_matkul.update({'matkul': matkul_to_predict,
                                     'status_matkul': status_matkul,
                                     'matkul_prasyarat': prasyarat[0]})
    context_prediktor_matkul = {**context, **context_prediktor_matkul}
    return context_prediktor_matkul


def get_evaluation_detail_message(jenjang, semester, evaluation_status):
    source = "Keputusan Rektor Universitas Indonesia\
            Nomor: 478/SK/R/UI/2004 tentang Evaluasi\
            Keberhasilan Studi Mahasiswa Universitas\
            Indonesia Pasal 11"
    putus_studi = {
        'S1': {
            '2': 'Apabila pada evaluasi 2 (dua) semester pertama \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari sekurang-kurangnya 24 \
                 (dua puluh empat) SKS terbaik',
            '4': 'Apabila pada evaluasi 4 (empat) semester pertama \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari sekurang-kurangnya 48 \
                 (empat puluh delapan) SKS terbaik',
            '8': 'Apabila pada evaluasi 8 (delapan) semester pertama \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari sekurang-kurangnya 96 \
                 (sembilan puluh enam) SKS terbaik',
            '12': 'Apabila pada evaluasi akhir masa studi \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari beban studi yang dipersyaratkan \
                 dengan nilai terendah C'
        },
        'S2': {
            '2': 'Apabila pada evaluasi 2 (dua) semester pertama \
                    tidak memperoleh indeks prestasi minimal 2,75 \
                    (dua koma tujuh puluh lima) dari sekurang-kurangnya 18 \
                    (delapan belas) SKS terbaik',
            '4': 'Apabila pada evaluasi akhir masa studi \
                tidak memperoleh indeks prestasi minimal 2,75 \
                (dua koma tujuh puluh lima) dari beban studi yang dipersyaratkan \
                dengan nilai terendah C'
        },
        'S3_S2': {
            '2': 'Apabila pada evaluasi 2 (dua) semester pertama \
                     tidak memperoleh indeks prestasi minimal 2,75 \
                     (dua koma tujuh puluh lima) dari jumlah SKS minimal \
                     yang dipersyaratkan',
            '4': 'Apabila pada evaluasi 4 (dua) semester pertama \
                    tidak berhasil lulus ujian kualifikasi  dan usulan \
                    penelitannya tidak memperoleh persetujuan panitia  \
                    penilai usulan penelitian untuk disertasi',
            '6': 'Apabila pada evaluasi 6 (enam) semester pertama \
                     tidak berhasil lulus ujian usulan penelitian dengan indeks prestasi minimal 2,75 \
                     (dua koma tujuh puluh lima) untuk semua mata kuliah yang dipersyaratkan',
            '10': 'Apabila pada evaluasi akhir masa studi (sepuluh semester)\
                     tidak memenuhi persyaratan untuk mengikuti ujian akhir pendidikan\
                     (ujian promosi doktor berupa penilaian terhadap disertasi)\
                      dengan indeks prestasi kumulatif dari beban studi \
                      yang dipersyaratkan minimal 2,75 (dua koma tujuh puluh lima)'
        },
        'S3_S1': {
            '4': 'Apabila pada evaluasi 4 (empat) semester pertama \
                     tidak memperoleh indeks prestasi minimal 2,75 \
                     (dua koma tujuh puluh lima) dari jumlah SKS minimal \
                     yang dipersyaratkan program studi',
            '5': 'Apabila pada evaluasi 5 (lima) semester pertama \
                    tidak berhasil lulus ujian kualifikasi  dan usulan \
                    penelitannya tidak memperoleh persetujuan panitia  \
                    penilai usulan penelitian untuk disertasi',
            '8': 'Apabila pada evaluasi 8 (delapan) semester pertama \
                     tidak berhasil lulus ujian usulan penelitian dengan indeks prestasi minimal 2,75 \
                     (dua koma tujuh puluh lima) untuk semua mata kuliah yang dipersyaratkan',
            '10': 'Apabila pada evaluasi akhir masa studi (sepuluh semester)\
                     tidak memenuhi persyaratan untuk mengikuti ujian akhir pendidikan\
                     (ujian promosi doktor berupa penilaian terhadap disertasi)\
                      dengan indeks prestasi kumulatif dari beban studi \
                      yang dipersyaratkan minimal 2,75 (dua koma tujuh puluh lima)'
        }
    }
    try:
        semester = str(semester)
        if evaluation_status == "tidak lolos" or evaluation_status == "hati-hati":
            return {"source": source, "detail": putus_studi[jenjang][semester]}
        else:
            return {"source": '-', "detail": '-'}
    except KeyError:
        return {"source": '-', "detail": '-'}


def get_semester_evaluation(kode_identitas, term):
    tahun = (datetime.now()).year
    angkatan = caching("get_angkatan", get_angkatan, (kode_identitas), kode_identitas)
    if angkatan == "Wrong kode identitas":
        return angkatan
    if term > 3 or term < 1:
        return "Wrong term"
    else:
        semester = (tahun - angkatan) * 2
    if semester == 6:
        semester = 8
    return semester


def get_semester_now(kode_identitas, term):
    tahun = (datetime.now()).year
    angkatan = caching("get_angkatan", get_angkatan, (kode_identitas), kode_identitas)
    if angkatan == "Wrong kode identitas":
        return angkatan
    if term > 3 or term < 1:
        return "Wrong term"
    elif term % 2 == 0 or term == 3:
        semester = (tahun - angkatan) * 2
    else:
        semester = ((tahun - angkatan) * 2) - 1
    return semester


def split_jenjang_and_jalur(str_jenjang):
    jenjang_array = str_jenjang.split(" ")
    if len(jenjang_array) != 2:
        return "Error Split Jenjang and Jalur"
    else:
        return jenjang_array[0]


def get_angkatan(kode_identitas):
    tahun = (datetime.now()).year
    try:
        kode_identitas = kode_identitas[:2]
        if int(kode_identitas[:1]) == 0:
            angkatan = int((str(tahun)[:3]) + kode_identitas[1:2])
        else:
            angkatan = int((str(tahun)[:2]) + kode_identitas)
        return angkatan
    except ValueError:
        return "Wrong kode identitas"


def get_index_mahasiswa_context(request, context):
    try:
        token, npm = request.session['access_token'], context['id']
        term = int(context['term'][-1:])
        if 'admin' not in request.session['user_login']:
            semester = caching("get_semester_evaluation", get_semester_evaluation, (npm, term), npm)
            sks_seharusnya = caching("get_sks_seharusnya", get_sks_seharusnya, (semester), npm)
            all_sks, err = caching("get_sks_sequential", get_sks_sequential,
                                   (request.session['access_token'], npm), npm)
            if err is None:
                sks_kurang = caching("get_sks_kurang",
                                     get_sks_kurang, (sks_seharusnya, all_sks), npm)
                status = caching("request_evaluation_status",
                                 request_evaluation_status, (npm, token, semester, all_sks), npm)
                context.update({'sks_seharusnya': sks_seharusnya,
                                'sks_kurang': sks_kurang, 'all_sks': all_sks,
                                'status': status, 'semester': semester,
                                'name': request.session['name']})
                context = {**context}
        elif request.session['user_login'] == 'admin':
            semester = 4
            sks_seharusnya = get_sks_seharusnya(semester)
            all_sks = 24
            sks_kurang = get_sks_kurang(sks_seharusnya, all_sks)
            status = request_evaluation_status(npm, token, semester, all_sks, 0)
            context.update({'sks_seharusnya': sks_seharusnya,
                            'sks_kurang': sks_kurang, 'all_sks': all_sks,
                            'status': status, 'semester': semester})
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_peraturan(request, context):
    try:
        token, npm = request.session['access_token'], context['id']
        term = int(context['term'][-1:])
        jenjang_str, err = caching("get_jenjang", get_jenjang, (token, npm), npm)
        if err is None:
            jenjang = caching("split_jenjang_and_jalur", split_jenjang_and_jalur, jenjang_str, npm)
            semester_now = caching("get_semester_now", get_semester_now, (npm, term), npm)
            semester_evaluation = caching("get_semester_evaluation",
                                          get_semester_evaluation, (npm, term), npm)
            status = caching("request_evaluation_status", request_evaluation_status,
                             (npm, token, semester_evaluation, 1), npm)
            detail_evaluasi = caching("get_evaluation_detail_message",
                                      get_evaluation_detail_message,
                                      (jenjang, semester_evaluation, status), npm)
            all_sks, err = caching("get_sks_sequential", get_sks_sequential,
                                   (request.session['access_token'], npm), npm)
            sks_seharusnya = caching("get_sks_seharusnya", get_sks_seharusnya,
                                     (semester_evaluation), npm)
            sks_kurang = caching("get_sks_kurang", get_sks_kurang,
                                 (sks_seharusnya, all_sks), npm)
            context.update({'all_sks': all_sks,
                            'semester_now': semester_now,
                            'semester_evaluation': semester_evaluation,
                            'sks_kurang': sks_kurang, 'name': request.session['name']})
            context = {**context, **detail_evaluasi}
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_riwayat_ip(request, context):
    try:
        token, npm = request.session['access_token'], context['id']
        graph_ip = caching("create_graph_ip", create_graph_ip, (token, npm), npm)
        context.update({'name': request.session['name']})
        context = {**context, **graph_ip}
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_riwayat_sks(request, context):
    try:
        token, npm = request.session['access_token'], context['id']
        sks_term = caching("convert_dict_for_sks_term",
                           convert_dict_for_sks_term, (token, npm), npm)
        all_sks, err = caching("get_sks_sequential",
                               get_sks_sequential,
                               (request.session['access_token'], npm), npm)
        if err is None:
            context.update({'sks_term': sks_term, 'all_sks': all_sks,
                            'name': request.session['name']})
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def convert_dict_for_sks_term(token, npm):
    sks_in_term = {}
    all_sks_term, err = caching("get_all_sks_term", get_all_sks_term, (token, npm), npm)
    if err is not None:
        return None
    for k, value in sorted(all_sks_term.items()):
        i = 1
        for val in value:
            new_key = str(k) + ' - ' + str(i)
            sks_in_term[new_key] = val
            i = i + 1
    return sorted(sks_in_term.items())


def convert_dict_for_ip_term(token, npm):
    ip_in_term = {}
    all_ip_term, err = caching("get_all_ip_term", get_all_ip_term, (token, npm), npm)
    if err is not None:
        return None
    for k, value in sorted(all_ip_term.items()):
        i = 1
        for val in value:
            new_key = str(k) + ' - ' + str(i)
            ip_in_term[new_key] = val
            i = i + 1
    return sorted(ip_in_term.items())


def create_graph_ip(token, npm):
    xdata = []
    ydata = []
    all_ip_term = caching("convert_dict_for_ip_term", convert_dict_for_ip_term, (token, npm), npm)
    for i in all_ip_term:
        xdata.append(i[0])
        ydata.append(i[1])
    chartdata = {
        'x': xdata, 'name1': 'IP', 'y1': ydata,
    }
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return data


def get_sks_seharusnya(semester):
    result = "semester bermasalah"
    if isinstance(semester, int):
        if semester != 6:
            result = 12 * semester
        else:
            result = 96
    return result


def get_sks_kurang(sks_seharusnya, all_sks):
    try:
        sks_kurang = sks_seharusnya - all_sks
        return sks_kurang
    except TypeError:
        return "sks seharusnya atau sks diperoleh bermasalah"


def get_profile(request, context):
    try:
        token = request.session['access_token']
        npm = context['id']
        mahasiswa, err = caching("get_data_user", get_data_user, (token, npm), npm)
        if err is None:
            last_term = len(mahasiswa['program']) - 1
            data_sks_dpo = caching("get_all_sks_term", get_all_sks_term, (token, npm), npm)[0]
            total_sks_dpo = 0

            for _, value in data_sks_dpo.items():
                for sks in value:
                    total_sks_dpo = total_sks_dpo + sks

            total_mutu = caching("get_total_mutu", get_total_mutu,
                                 (request.session['access_token'], npm), npm)[0]
            ipk = total_mutu / total_sks_dpo
            prodi = mahasiswa['program'][last_term]['nm_org'] + \
                    ", " + mahasiswa['program'][0]['nm_prg']
            context.update({'angkatan': mahasiswa['program'][last_term]['angkatan'],
                            'prodi': prodi,
                            'status': mahasiswa['program'][last_term]['nm_status'],
                            'sks_lulus': caching("get_sks_sequential",
                                                 get_sks_sequential,
                                                 (request.session['access_token'], npm), npm)[0],
                            'mutu': str(round(total_mutu, 2)),
                            'ipk': str(round(ipk, 2)),
                            'sks_diperoleh': total_sks_dpo})
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_rekomendasi_context(request, context_mahasiswa):
    try:
        npm = context_mahasiswa['id']
        # print("NPM", npm)
        if request is not None:
            prediksi_list = get_recommendation(npm)
            # print("PREDIKSI_LIST", prediksi_list)
            page = request.GET.get('page', 1)
            # print("PAGE", page)
            answers_list = list(prediksi_list)
            # print("ANSWER_LIST", answers_list)
            paginator = Paginator(answers_list, 10)
            # print("PAGINATOR", paginator)
            try:
                prediksi = paginator.page(page)
            except EmptyPage:
                prediksi = paginator.page(paginator.num_pages)
            # print("PREDIKSI", prediksi)
            context_mahasiswa.update({'table': prediksi})
            # print("CONTEXT_MAHASISWA", context_mahasiswa)
            return context_mahasiswa
        else:
            # print("CONTEXT_MAHASISWA", context_mahasiswa)
            return context_mahasiswa
    except KeyError:
        return {}
