<<<<<<< HEAD
from django.shortcuts import render


def prediktor_matkul(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/prediktor-matkul.tpl', context)
=======
from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import get_term, get_context_mahasiswa


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
>>>>>>> ac1e53e5d5183d390fcb3982b7fe24f1cf580fd0
