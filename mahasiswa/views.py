from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import get_term, get_context_mahasiswa, get_semester
from api.apps import give_verdict

# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        # evaluasi_akademik()
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)

def evaluasi_akademik():
    # now = datetime.now()
    # term_str = get_term(now)
    # semester = get_semester(context['id'], int(term_str))
    # sks_diperoleh = 48
    # sks_diambil = 20
    # ip = 4.0
    pass