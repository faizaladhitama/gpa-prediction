from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'name':'sekre'}
	return render(request, 'sekre/index.tpl', context)