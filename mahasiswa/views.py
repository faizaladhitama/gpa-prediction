from datetime import datetime

from django.shortcuts import render

from api.db.utils import caching
from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context, get_riwayat_sks, get_riwayat_ip, \
    get_peraturan, get_profile, get_prediktor_matkul_context
# Create your views here.


def index(request):
    now = datetime.now()
    year = now.year
    term = 1
    if now.month < 8:
        year = now.year - 1
        term = 3
        if now.month > 2 and now.month < 7:
            term = 2
    term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = caching("get_index_mahasiswa_context",
                          get_index_mahasiswa_context, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        prediktor_matkul_context = get_prediktor_matkul_context(request, 'IKO31300', context)
        return render(request, 'mahasiswa/index.tpl', context)
    except TypeError as err_msg:
        print('ini eror' + str(err_msg))
        return render(request, 'landing_page.tpl', {})


def profile(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_profile(request, context_mahasiswa)
        # context = caching("get_profile",
        #                   get_profile, (request, context_mahasiswa),
        #                   context_mahasiswa['id'])
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
        # context = caching("get_riwayat_sks",
        #                   get_riwayat_sks, (request, context_mahasiswa),
        #                   context_mahasiswa['id'])
        return render(request, 'mahasiswa/sks-term-table.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def riwayat_ip(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_riwayat_ip(request, context_mahasiswa)
        # context = caching("get_riwayat_ip", get_riwayat_ip,
        #                   (request, context_mahasiswa),
        #                   context_mahasiswa['id'])
        return render(request, 'mahasiswa/graph-ip_term.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def peraturan_akademik(request):
    now = datetime.now()
    term_str = get_term(now)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_peraturan(request, context_mahasiswa)
        # context = caching("get_peraturan", get_peraturan,
        #                   (request, context_mahasiswa),
        #                   context_mahasiswa['id'])
        return render(request, 'mahasiswa/peraturan-akademik.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def prediksi_matkul(request):
    now = datetime.now()
    year = now.year
    term = 1
    if now.month < 8:
        year = now.year - 1
        term = 3
        if now.month > 2 and now.month < 7:
            term = 2
    term_str = str(year) + "/" + str(year + 1) + " - " + str(term)
    try:
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = caching("get_index_mahasiswa_context",
                          get_index_mahasiswa_context, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        prediktor_matkul_context = get_prediktor_matkul_context(request, 'IKO31300', context)
        return render(request, 'mahasiswa/prediktor-matkul.tpl', context)
    except TypeError as err_msg:
        print('ini eror' + str(err_msg))
        return render(request, 'landing_page.tpl', {})