from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'name': 'sekre'}
    return render(request, 'sekre/index.tpl', context)


def profile(request):
    context = {'name': 'sekre'}
    return render(request, 'sekre/profile.tpl', context)


def cari_mahasiswa(request):
    context = {'name': 'sekre'}
    return render(request, 'sekre/cari-mahasiswa.tpl', context)
