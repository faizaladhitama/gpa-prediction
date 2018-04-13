from datetime import datetime
<<<<<<< HEAD

from api.apps import give_verdict

from api.siak import get_jenjang


=======
from api.apps import give_verdict, save_status
from api.siak import get_access_token, get_sks
>>>>>>> 78f2284c9399c75ecf9eb4f7e5aef0bf4c310500
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


def get_evaluation_status(npm, term, sks_lulus, sks_diambil, ip_now=3.0):
    if(term == 5 or term == 6): #semester 5 dan 6 tidak ada evaluasi
        term = 8
    elif term % 2 > 0:
        term = term+1 #evaluasi dilakukan di semester genap,jdi sks min nya disesuaikan
    sks_minimal = 12*term #still a temporary form , will be integrated with proper flow later
    status = give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_now)
    save_status(npm, status)
    return status

def request_evaluation_status(npm, username, password, term):
    token = get_access_token(username, password)
    sks_lulus = get_sks(token, npm)[0]
    sks_diambil = 18
    ip_now = 3.0 #diitung ntr
    status = get_evaluation_status(npm, term, sks_lulus, sks_diambil, ip_now)
    save_status(npm, status)
    return status


def get_evaluation_detail_message(jenjang, semester):
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
            '4': 'Apabila pada evaluasi 4 (dua) semester pertama \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari sekurang-kurangnya 48 \
                 (dua puluh empat) SKS terbaik',
            '8': 'Apabila pada evaluasi 2 (dua) semester pertama \
                 tidak memperoleh indeks prestasi minimal 2,0 \
                 (dua koma nol) dari sekurang-kurangnya 96 \
                 (dua puluh empat) SKS terbaik',
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
        return {"source": source, "detail": putus_studi[jenjang][semester]}
    except KeyError:
        return "Wrong degree and semester"


def get_semester(kode_identitas, term):
    tahun = (datetime.now()).year
    angkatan = get_angkatan(kode_identitas)
    if angkatan == "Wrong kode identitas":
        return angkatan
    if (term > 3 or term < 1):
        return "Wrong term"
    else:
        semester = tahun - angkatan
        if term % 2 == 0 or term == 3:
            semester = semester * 2
        else:
            semester = (semester * 2) - 1
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


def get_index_mahasiswa_context(request, context, term_str):
    try:
        if context['id'] == 'admin':
            return context
        else:
            jenjang_str, err = get_jenjang(request.session['access_token'],
                                           context['id'])
            if err is not None:
                return None
            else:
                jenjang = split_jenjang_and_jalur(jenjang_str)
                evaluation_message = get_evaluation_detail_message(
                    jenjang, int(term_str[-1:]))
                detail_evaluation = {'detail': evaluation_message}
                context.update(detail_evaluation)
                return context
    except KeyError as excp:
        return str(excp)
    except AttributeError as excp:
        return str(excp)
