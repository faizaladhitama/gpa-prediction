from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import request_evaluation_status, get_semester, get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context

from api.siak import get_access_token, get_data_user, get_all_sks_term


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    token = get_access_token(username, password)
   
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_index_mahasiswa_context(request, context_mahasiswa,
                                              term_str)
        npm = context_mahasiswa['kode_identitas']
        username = context_mahasiswa['user']
        password = 'aa'
        sks_seharusnya = 12*term
        context.update({'sks_seharusnya' : sks_seharusnya})
        sks_kurang = sks_seharusnya - get_all_sks_term(token, npm)
        context.update({'sks_kurang' : sks_kurang})
        status = request_evaluation_status(npm, username, password, term)
        context.update({'status' : status})
        semester = get_semester(npm, term_str)
        context.update({'semester' : semester})
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
