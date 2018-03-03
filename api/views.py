from django.shortcuts import render

# Create your views here.
def index(request):
	#context : passing args to template
    context = {'team':'usagi studio'}
    return render(request, 'api/index.tpl', context)

def login(request):
    context = {'team':'usagi studio'}
    return render(request, 'login.tpl',context)