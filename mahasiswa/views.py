from django.shortcuts import render


def prediktor_matkul(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/prediktor-matkul.tpl', context)
