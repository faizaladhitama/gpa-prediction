from datetime import datetime

from django.shortcuts import render

from api.db.utils import caching
from api.siak import get_data_user, \
    get_all_sks_term, get_total_mutu, get_sks_sequential
from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context, get_riwayat_sks, get_riwayat_ip, \
    get_peraturan
# Create your views here.


def index(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = caching("get_index_mahasiswa_context",
                          get_index_mahasiswa_context, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError:

        return render(request, 'landing_page.tpl', {})


def profile(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context = get_context_mahasiswa(request, term_str)
        npm = context['id']

        token = request.session['access_token'] or ""
        mahasiswa, err = caching("get_data_user", get_data_user, (token, npm), npm)
        if err:
            raise TypeError
        # print("Profile mahasiswa", mahasiswa)
        last_term = len(mahasiswa['program'])-1
        data_sks_dpo = caching("get_all_sks_term", get_all_sks_term, (token, npm), npm)[0]
        total_sks_dpo = 0

        for _, value in data_sks_dpo.items():
            for sks in value:
                total_sks_dpo = total_sks_dpo + sks

        total_mutu = caching("get_total_mutu", get_total_mutu,
                             (request.session['access_token'], npm), npm)[0]
        ipk = total_mutu/total_sks_dpo
        data_mahasiswa = {}
        data_mahasiswa['nama'] = mahasiswa['nama'].lower().title()
        data_mahasiswa['npm'] = mahasiswa['npm']
        data_mahasiswa['angkatan'] = mahasiswa['program'][last_term]['angkatan']
        data_mahasiswa['prodi'] = mahasiswa['program']\
            [last_term]['nm_org'] + ", " + mahasiswa['program'][0]['nm_prg']
        data_mahasiswa['status'] = mahasiswa['program'][last_term]['nm_status']
        data_mahasiswa['sks_lulus'] = caching("get_sks_sequential",
                                              get_sks_sequential,
                                              (request.session['access_token'], npm), npm)[0]
        data_mahasiswa['mutu'] = str(round(total_mutu, 2))
        data_mahasiswa['ipk'] = str(round(ipk, 2))
        data_mahasiswa['sks_diperoleh'] = total_sks_dpo
        context.update({'data_mahasiswa': data_mahasiswa})
        return render(request, 'mahasiswa/profile.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)


def riwayat_sks(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_riwayat_sks(request, context_mahasiswa)
        return render(request, 'mahasiswa/sks-term-table.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def riwayat_ip(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_riwayat_ip(request, context_mahasiswa)
        return render(request, 'mahasiswa/graph-ip_term.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def peraturan_akademik(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_peraturan(request, context_mahasiswa)
        return render(request, 'mahasiswa/peraturan-akademik.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})
