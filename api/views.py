from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .siak import get_access_token, verify_user


def landing(request):
    context = {'team': 'usagi studio'}
    return render(request, 'landing_page.tpl', context)


def login(request):
    return render(request, 'api/login.tpl', {})


def auth_login(request):
    print("#==> auth_login ", request.method)
    try:
        username = request.POST['username']
        password = request.POST['password']
        access_token = get_access_token(username, password)
        connection = True
        if 'connection' in request.POST:
            connection = False
        if "ConnectionError" in access_token or not connection:
            messages.error(request, "Server UI sedang down")
            return HttpResponseRedirect(reverse('api:landing'))
        try:
            ver_user = verify_user(access_token)
            kode_identitas = ver_user['identity_number']
            role = ver_user['role']
            request.session['user_login'] = username
            request.session['access_token'] = access_token
            request.session['kode_identitas'] = kode_identitas
            request.session['role'] = role
            # messages.success(request, "Anda berhasil login " + username)
            return HttpResponseRedirect(reverse('mahasiswa:index'))
        except KeyError:
            messages.error(request, "Username atau password salah")
            return HttpResponseRedirect(reverse('api:landing'))
    except KeyError:
        return render(request, 'blank.tpl', {})


def auth_logout(request):
    print("#==> auth logout")
    request.session.flush()  # menghapus semua session\
    # messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('api:landing'))


def index(request):
    return render(request, 'blank.tpl', {})
