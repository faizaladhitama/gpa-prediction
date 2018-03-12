from django.shortcuts import render
from api.models import Civitas
from api.models import Mahasiswa
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	#context : passing args to template
    context = {'team':'usagi studio'}
    return render(request, 'api/index.tpl', context)

def login(request):
	if request.user == None:
		user = "None"
	else:
		user = request.user
		user_django_id = list(User.objects.filter(username=user))[0].id
		civitas = list(Civitas.objects.filter(user_id=user_django_id))[0]
		mahasiswa = list(Mahasiswa.objects.filter(civitas_ptr_id=civitas.id))[0]
		print(mahasiswa.peran_user)
	context={'team':'usagi studio','user':user,'peran':mahasiswa.peran_user}
	return render(request, 'mahasiswa/index.tpl',context)