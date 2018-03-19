import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .siak import get_access_token, verify_user, get_data_user


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
        try:
            ver_user = verify_user(access_token)
            kode_identitas = ver_user['identity_number']
            role = ver_user['role']
            request.session['user_login'] = username
            request.session['access_token'] = access_token
            request.session['kode_identitas'] = kode_identitas
            request.session['role'] = role
            messages.success(request, "Anda berhasil login " + username)
            return HttpResponseRedirect(reverse('api:index'))
        except KeyError:
            messages.error(request, "Username atau password salah")
            return HttpResponseRedirect(reverse('api:landing'))
    except KeyError:
        return render(request, 'blank.tpl', {})


def auth_logout(request):
    print("#==> auth logout")
    request.session.flush()  # menghapus semua session\
    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('api:landing'))


def index(request):
    try:
        now = datetime.datetime.now()
        if now.month < 8:
            year = now.year - 1
            if now.month > 2 and now.month < 7:
                term = 2
            else:
                term = 3
        else:
            year = now.year
            term = 1
        term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
        get_data_user(request.session['access_token'], request.session['kode_identitas'])
        context = {
            'term': term_str,
            'team': 'usagi studio',
            'user': request.session['user_login'],
            'id': request.session['kode_identitas'],
            'role': request.session['role']
        }
        return render(request, 'mahasiswa/index.tpl', context)
    except KeyError:
        return render(request, 'landing_page.tpl', {})
