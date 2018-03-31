from django.shortcuts import render

<<<<<<< HEAD

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    year = now.year
    term = 1
    if now.month < 8:
        year = now.year - 1
        term = 3
        if now.month > 2 and now.month < 7:
            term = 2
    term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
    try:
        context = {
            'term': term_str,
            'team': 'usagi studio',
            'user': request.session['user_login'],
            'id': request.session['kode_identitas'],
            'role': request.session['role']
        }
        return render(request, 'mahasiswa/index.tpl', context)
    except KeyError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)

=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87

def prediktor_matkul(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/prediktor-matkul.tpl', context)
