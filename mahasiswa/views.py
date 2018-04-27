import traceback
from datetime import datetime

from django.shortcuts import render

from api.siak import get_sks, get_jenjang, get_data_user, get_all_sks_term
from mahasiswa.utils import get_term, get_context_mahasiswa, \
     get_index_mahasiswa_context, get_semester, request_evaluation_status


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
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        npm = context['id']
        mahasiswa = get_data_user(request.session['access_token'], npm)
        last_term = len(mahasiswa[0]['program'])-1

        data_sks_dpo = get_all_sks_term(request.session['access_token'], npm)[0]
        total_sks_dpo = 0

        for key, value in data_sks_dpo.items():
            for sks in value:
                total_sks_dpo = total_sks_dpo + sks

        data_mahasiswa = {}
        data_mahasiswa['nama'] = mahasiswa[0]['nama'].lower().title()
        data_mahasiswa['npm'] = mahasiswa[0]['npm']
        data_mahasiswa['angkatan'] = mahasiswa[0]['program'][last_term]['angkatan']
        data_mahasiswa['prodi'] = mahasiswa[0]['program']\
        [last_term]['nm_org'] + ", " + mahasiswa[0]['program'][0]['nm_prg']
        data_mahasiswa['status'] = mahasiswa[0]['program'][last_term]['nm_status']
        data_mahasiswa['sks_lulus'] = get_sks(request.session['access_token'], npm)[0]
        # data_mahasiswa['mutu'] =
        # data_mahasiswa['ipk'] =
        data_mahasiswa['sks_diperoleh'] = total_sks_dpo
        context.update({'data_mahasiswa': data_mahasiswa})
        # print(mahasiswa)
        print(data_mahasiswa) 
         
        return render(request, 'mahasiswa/profile.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)
