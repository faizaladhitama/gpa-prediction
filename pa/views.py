from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'name':'pa'}
	return render(request, 'pa/index.tpl', context)

def profile(request):
	context = {'name':'pa'}
	return render(request, 'pa/profile.tpl', context)

def cari_mahasiswa(request):
	context = {'name':'pa'}
	return render(request, 'pa/cari-mahasiswa.tpl', context)