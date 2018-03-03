from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'name':'pa'}
	return render(request, 'pa/index.tpl', context)