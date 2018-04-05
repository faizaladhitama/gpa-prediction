def get_term(datetime):
    year = datetime.year
    term = 1
    if datetime.month < 8:
        year = datetime.year - 1
        term = 3
        if datetime.month > 2 and datetime.month < 7:
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
        return {"source": source, "detail": putus_studi[jenjang][semester]}
    except KeyError:
        return "Wrong jenjang and semester"


def get_semester():
    """
    term_str = get_term()
    kode_identitas = request.session['kode_identitas']
    angkatan = int(kode_identitas[2:])
    year = int(term_str[5:-4])
    term = int(term_str[-1:])
    return
    """
    pass


def get_evaluation_status():
    pass


def get_total_credits():
    pass
