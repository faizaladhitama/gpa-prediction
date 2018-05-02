import multiprocessing as mp
import time
from collections import OrderedDict
from datetime import datetime

import django

django.setup()

from api.utils import give_verdict, save_status
from api.siak import get_jenjang, get_all_sks_term, \
    get_all_ip_term, get_sks, get_sks_sequential


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
        context = {
            'term': term_str,
            'team': 'usagi studio',
            'user': request.session['user_login'],
            'id': request.session['kode_identitas'],
            'role': request.session['role']
        }
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def get_evaluation_status(term, sks_lulus, sks_diambil, ip_now=3.0):
    if term % 2 > 0:
        term = term + 1  # evaluasi dilakukan di semester genap,jdi sks min nya disesuaikan
    sks_minimal = 12 * term  # still a temporary form , will be integrated with proper flow later
    status = give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_now)
    return status


def request_evaluation_status(npm, token, term, sks_lulus=-1, mode=0):
    if sks_lulus < 0:
        if mode == 1:
            sks_lulus = get_sks_sequential(token, npm)[0]
        else:
            sks_lulus = get_sks(token, npm)[0]
    sks_diambil = 18
    ip_now = 3.0  # diitung ntr
    try:
        status = get_evaluation_status(term, sks_lulus, sks_diambil, ip_now)
        save_status(npm, status)
        return status
    except TypeError:
        return "Argument salah"


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
    angkatan = get_angkatan(kode_identitas)
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
    angkatan = get_angkatan(kode_identitas)
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
        pool = mp.Pool(processes=mp.cpu_count() * 2, maxtasksperchild=2)
        token, npm = request.session['access_token'], context['id']
        term = int(context['term'][-1:])

        # Sequential
        # semester = get_semester_evaluation(npm, term)
        # sks_seharusnya = get_sks_seharusnya(semester)
        # all_sks, err = get_sks(request.session['access_token'], npm)
        # if err is None:
        #     sks_kurang = get_sks_kurang(sks_seharusnya, all_sks)
        #     status = request_evaluation_status(npm, token, semester, all_sks)
        #     context.update({'sks_seharusnya': sks_seharusnya,
        #                     'sks_kurang': sks_kurang, 'all_sks': all_sks,
        #                     'status': status, 'semester': semester})

        start = time.clock()
        # print("a")
        semester = pool.apply_async(get_semester_evaluation, args=(npm, term,)).get(timeout=5)
        # print("b")
        sks_seharusnya = pool.apply_async(get_sks_seharusnya, args=(semester,)).get(timeout=5)
        # print("c")
        all_sks, err = get_sks(request.session['access_token'], npm)
        # all_sks, err = pool.apply_async(get_sks_sequential,
        #                                 args=(request.session['access_token'],
        #                                       npm,)).get(timeout=20)
        # print("d")
        if err is None:
            sks_kurang = pool.apply_async(get_sks_kurang,
                                          args=(sks_seharusnya, all_sks)).get(timeout=5)
            # print("e")
            status = pool.apply_async(request_evaluation_status,
                                      args=(npm, token, semester, all_sks, 0)).get(timeout=5)
            # print("f")
            context.update({'sks_seharusnya': sks_seharusnya,
                            'sks_kurang': sks_kurang, 'all_sks': all_sks,
                            'status': status, 'semester': semester})
            # print("g")
        print(time.clock() - start)
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)
    except TypeError as excp:
        return str(excp)


def get_rekam_akademik_index(request, context):
    try:
        pool = mp.Pool(processes=mp.cpu_count() * 2, maxtasksperchild=2)
        token, npm = request.session['access_token'], context['id']
        term = int(context['term'][-1:])
        start = time.clock()

        jenjang_str, err = pool.apply_async(get_jenjang, args=(token, npm,)).get(timeout=10)
        # print("a")
        if err is None:
            jenjang = pool.apply_async(split_jenjang_and_jalur, args=(jenjang_str,))
            sks_term = pool.apply_async(convert_dict_for_sks_term, args=(token, npm,))
            # print("c")
            graph_ip = pool.apply_async(create_graph_ip, args=(token, npm,))
            # print("d")
            semester_now = pool.apply_async(get_semester_now, args=(npm, term,))
            # print("e")
            semester_evaluation = pool.apply_async(get_semester_evaluation,
                                                   args=(npm, term,))
            # print("f")
            status = pool.apply_async(request_evaluation_status,
                                      args=(npm, token, semester_evaluation.get(timeout=10), 1,))
            # status = request_evaluation_status(npm, token, semester_evaluation)
            # print("g")
            detail_evaluasi = pool.apply_async(get_evaluation_detail_message,
                                               args=(jenjang.get(timeout=20),
                                                     semester_evaluation.get(
                                                         timeout=20),
                                                     status.get(timeout=40),))
            
            # print("h")
            # all_sks, err = pool.apply_async(get_sks_sequential,
            #                                 args=(request.session['access_token'],
            #                                       npm,)).get(timeout=20)
            all_sks, err = get_sks(request.session['access_token'], npm)
            # print("i")
            sks_seharusnya = pool.apply_async(get_sks_seharusnya,
                                              args=(semester_evaluation.get(timeout=10),))
            # print("j")
            sks_kurang = pool.apply_async(get_sks_kurang,
                                          args=(sks_seharusnya.get(timeout=10), all_sks))
            # print("k")
            context.update({'sks_term': sks_term.get(timeout=10), 'all_sks': all_sks,
                            'semester_now': semester_now.get(timeout=10),
                            'semester_evaluation': semester_evaluation.get(timeout=10),
                            'sks_kurang': sks_kurang.get(timeout=10)})
            # print("l")
            context = {**context, **detail_evaluasi.get(timeout=20), **graph_ip.get(timeout=20)}
            # print("m")
        print(time.clock() - start)
        return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)


def convert_dict_for_sks_term(token, npm):
    sks_in_term = OrderedDict()
    all_sks_term, err = get_all_sks_term(token, npm)
    if err is not None:
        return None
    for k, value in sorted(all_sks_term.items()):
        i = 1
        for val in value:
            new_key = str(k) + ' - ' + str(i)
            sks_in_term[new_key] = val
            i = i + 1
    return sks_in_term


def convert_dict_for_ip_term(token, npm):
    ip_in_term = OrderedDict()
    all_ip_term, err = get_all_ip_term(token, npm)
    if err is not None:
        return None
    for k, value in sorted(all_ip_term.items()):
        i = 1
        for val in value:
            new_key = str(k) + ' - ' + str(i)
            ip_in_term[new_key] = val
            i = i + 1
    return ip_in_term


def create_graph_ip(token, npm):
    """
    discretebarchart page
    """
    xdata = []
    ydata = []
    all_ip_term = convert_dict_for_ip_term(token, npm)
    for key, value in all_ip_term.items():
        xdata.append(key)
        ydata.append(value)
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
