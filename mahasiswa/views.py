from datetime import datetime

from django.shortcuts import render

from api.siak import get_all_sks_term
from mahasiswa.utils import request_evaluation_status, get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_index_mahasiswa_context(request, context_mahasiswa,
                                              term_str)
        npm = request.session['kode_identitas']
        username = context_mahasiswa['user']
        password = 'aa'
        sks_seharusnya = 12 * 1
        sks_kurang = sks_seharusnya - get_all_sks_term(request.session['access_token'], npm)
        context.update({'sks_kurang': sks_kurang})
        status = request_evaluation_status(npm, username, password, 1)
        context.update({'status': status})
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
