from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'name': 'dosen'}
    return render(request, 'dosen/index.tpl', context)


def profile(request):
    context = {'name': 'dosen'}
    return render(request, 'dosen/profile.tpl', context)


def cari_mahasiswa(request):
    context = {'name': 'dosen'}
    return render(request, 'dosen/cari-mahasiswa.tpl', context)
