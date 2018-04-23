from datetime import datetime

from django.shortcuts import render

from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context, get_semester, request_evaluation_status

from api.siak import get_sks, get_all_sks_term


# Create your views here.
def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context, err = get_index_mahasiswa_context(request, context_mahasiswa)
        npm = context_mahasiswa['id']
        username = context_mahasiswa['user']
        term = int(term_str[-1:])
        semester = get_semester(npm, term)
        if semester != 6:
            sks_seharusnya = 12 * semester
        else:
            sks_seharusnya = 96
        context.update({'sks_seharusnya': sks_seharusnya})
        all_sks, err = get_sks(request.session['access_token'], npm)
        if err is not None and username != "admin":
            print(err)
        if username != "admin":
            sks_kurang = sks_seharusnya - all_sks
            context.update({'sks_kurang' : sks_kurang})
            status = request_evaluation_status(npm, request.session['access_token'], semester)
            context.update({'status' : status})
            context.update({'semester' : semester})
            all_sks_term, err = get_all_sks_term(request.session['access_token'], npm)
            context.update({'sks_term': all_sks_term})
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def profile(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/profile.tpl', context)


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
