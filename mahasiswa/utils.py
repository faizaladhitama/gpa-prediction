def getTerm(datetime):
    year = datetime.year
    term = 1
    if datetime.month < 8:
        year = datetime.year - 1
        term = 3
        if datetime.month > 2 and datetime.month < 7:
            term = 2
    term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
    return term_str


def getContextMahasiswa(request, term_str):
    context = {
        'term': term_str,
        'team': 'usagi studio',
        'user': request.session['user_login'],
        'id': request.session['kode_identitas'],
        'role': request.session['role']
    }
    return context
