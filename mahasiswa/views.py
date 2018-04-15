from datetime import datetime
from traceback import print_exc
from django.shortcuts import render
from mahasiswa.utils import request_evaluation_status, get_semester, \
    get_term, get_context_mahasiswa, get_index_mahasiswa_context
from api.siak import get_sks


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
        term = int(term_str[-1:])
        semester = get_semester(npm, term)
        if semester != 6:
            sks_seharusnya = 12*semester
        else:
            sks_seharusnya = 96
        context.update({'sks_seharusnya' : sks_seharusnya})
        all_sks, err = get_sks(request.session['access_token'], npm)
        if err is not None:
            print(err)
        print(str(all_sks))
        sks_kurang = sks_seharusnya - all_sks
        context.update({'sks_kurang' : sks_kurang})
        status = request_evaluation_status(npm, username, term)
        context.update({'status' : status})
        context.update({'semester' : semester})
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        print_exc()
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
