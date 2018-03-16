import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Mahasiswa, Civitas
from .sso.csui_helper import get_access_token, verify_user, get_client_id, get_data_user
from .api_dev import *


def landing(request):

    context = {'team': 'usagi studio'}
    return render(request, 'landing_page.tpl', context)

def login(request):
    return render(request, 'api/login.tpl', {})

def auth_login(request):
    print("#==> auth_login ", request.method)

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
            return HttpResponseRedirect(reverse('api:landing'))

def auth_logout(request):
    print("#==> auth logout")
    request.session.flush() # menghapus semua session\
    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('api:landing'))

def index(request):
    now = datetime.datetime.now()
    term = 0
    if now.month < 8:
        year = now.year - 1
        if now.month > 2 and now.month < 7:
            term = 2
        else:
            term = 3
    else:
        year = now.year
        term = 1
    term_str = str(year)+"/"+str(year+1)+" - "+str(term)
    get_data_user(request.session['access_token'], request.session['kode_identitas'])
    context = {
        'term':term_str,
        'team':'usagi studio',
        'user':request.session['user_login'],
        'id':request.session['kode_identitas'],
        'role':request.session['role']
    }
    """
    if mobileBrowser(request):
        t = 'mahasiswa/index.tpl'
    else:
        t = 'mahasiswa/mobile/index.tpl'
    """
    return render(request, 'mahasiswa/index.tpl', context)
