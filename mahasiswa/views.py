from datetime import datetime

from django.shortcuts import render

from api.siak import get_sks, get_jenjang, get_data_user
from mahasiswa.utils import get_term, get_context_mahasiswa, \
     get_index_mahasiswa_context, get_semester, request_evaluation_status


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        # mahasiswa = get_data_user(request.session['access_token'], npm)
         
        return render(request, 'mahasiswa/profile.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
