from datetime import datetime
from django.shortcuts import render
from mahasiswa.utils import getTerm, getContextMahasiswa


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = getTerm(now)
    try:
        context = getContextMahasiswa(request,term_str)
        return render(request, 'mahasiswa/index.tpl', context)
    except KeyError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
