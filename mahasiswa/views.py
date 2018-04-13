from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import request_evaluation_status, get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context

from api.siak import get_access_token, get_data_user, get_all_sks_term


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_index_mahasiswa_context(request, context_mahasiswa,
                                              term_str)
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)


def get_evaluation_status():
    now = datetime.now()
    term_str = get_term(now)
    token = get_access_token(username, password)
    context_mahasiswa = get_context_mahasiswa(request, term_str)
    npm = context_mahasiswa['kode_identitas']
    username = context_mahasiswa['user']
    pwd = 'aa'
    status = request_evaluation_status(npm, username, password, term)
    if status == 'lolos':
        status_button = '<button type="button" class="btn btn-success btn-lg btn3d">lolos</button>'
        return HttpResponse(status_button, sks_kurang)
    elif status == 'hati-hati':
        status_button = '<button type="button" class="btn btn-warning btn-lg btn3d">hati-hati</button>'
        sks_seharusnya = 12*term
        sks_kurang = sks_seharusnya - get_all_sks_term(token, npm)
        return HttpResponse(status_button, sks_kurang)
    else:
        status_button = '<button type="button" class="btn btn-success btn-lg btn3d">tidak <br>lolos</button>'
        sks_kurang = sks_seharusnya - get_all_sks_term(token, npm)
        return HttpResponse(status_button, sks_kurang)