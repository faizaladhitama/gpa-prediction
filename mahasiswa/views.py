import traceback
from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context

# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_index_mahasiswa_context(request, context_mahasiswa)
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        traceback.print_exc()
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
