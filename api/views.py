from django.shortcuts import render
from .models import Mahasiswa, Civitas
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .sso.csui_helper import get_access_token, verify_user, get_client_id
from .api_dev import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def dummy(request):
    # context : passing args to template
    context = {'team': 'usagi studio'}
    return render(request, 'api/index.tpl', context)


def index(request):
    """
    if request.user is None:
        user = "None"
    else:
        user = request.user
        user = list(User.objects.filter(username=user))[0]
        civitas = list(Civitas.objects.filter(user_id=user.id))[0]
        mahasiswa = list(Mahasiswa.objects.filter(civitas_ptr_id=civitas.id))[0]
        print(mahasiswa)
    """
    context = {'team': 'usagi studio'}
    if 'user_login' in request.session.keys():
        print("masuk")
        cari_info_program(request.session['kode_identitas'],get_client_id(),request.session['access_token'])
    return render(request, 'login.tpl', context)

def login(request):
    context = {'team': 'usagi studio'}
    print(request.session)
    return render(request, 'api/prima_login.tpl', context)

def auth_login(request):
    print ("#==> auth_login ",request.method)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #call csui_helper
        access_token = get_access_token(username, password)
        print(access_token)
        if access_token is not None:
            ver_user = verify_user(access_token)
            kode_identitas = ver_user['identity_number']
            role = ver_user['role']

            # set session
            request.session['user_login'] = username
            request.session['access_token'] = access_token
            request.session['kode_identitas'] = kode_identitas
            request.session['role'] = role
            messages.success(request, "Anda berhasil login "+username)
            return HttpResponseRedirect(reverse('api:index'))
        else:
            messages.error(request, "Username atau password salah")

def auth_logout(request):
    print ("#==> auth logout")
    request.session.flush() # menghapus semua session

    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('api:index'))

