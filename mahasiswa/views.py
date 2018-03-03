from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'name':'mahasiswa'}
	return render(request, 'mahasiswa/index.tpl', context)