from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/index.tpl', context)


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
