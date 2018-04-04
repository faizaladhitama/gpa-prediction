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

def get_evaluation_detail_message(message):
    """
    sumber = "Keputusan Rektor Universitas Indonesia"
    "Nomor: 478/SK/R/UI/2004 tentang Evaluasi "
    "Keberhasilan Studi Mahasiswa Universitas "
    "Indonesia Pasal 11"
    """
    putus_akademik = {
        'IP': 'Apabila pada evaluasi akhir '
              'masa studi tidak memperoleh indeks '
              'prestasi minimal 2,0 (dua koma nol) '
              'dari beban studi yang dipersyaratkan '
              'dengan nilai terendah C.',
        'SKS' :{
            '2': 'Apabila pada evaluasi 2 (dua) '
                 'semester pertama tidak memperoleh '
                 'indeks prestasi minimal 2,0 (dua koma '
                 'nol) dari sekurang-kurangnya 24 (dua '
                 'puluh empat) SKS terbaik;',
            '4': 'Apabila pada evaluasi 4 (empat) '
                 'semester pertama tidak memperoleh indeks '
                 'prestasi minimal 2,0 (dua koma nol) dari '
                 'sekurang-kurangnya 48 (empat puluh delapan) '
                 'SKS terbaik;',
            '8': 'Apabila pada evaluasi 2 (dua) '
                 'semester pertama tidak memperoleh indeks '
                 'prestasi minimal 2,0 (dua koma nol) dari '
                 'sekurang-kurangnya 24 (dua puluh empat) '
                 'SKS terbaik;'
            }
    }
    if "IP" in message:
        return putus_akademik['IP']
    else:
        return None

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
