from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'name':'dosen'}
	return render(request, 'dosen/index.tpl', context)