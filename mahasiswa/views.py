from datetime import datetime

from django.shortcuts import render
from django_tables2 import RequestConfig
from api.db.utils import caching
from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context, get_riwayat_sks, get_riwayat_ip, \
    get_peraturan, get_profile, set_npm, get_recommendation
from mahasiswa.table import RekomendasiTable


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
        context_mahasiswa = get_context_mahasiswa(request, term_str)
        context = get_profile(request, context_mahasiswa)
        # context = caching("get_profile",
        #                   get_profile, (request, context_mahasiswa),
        #                   context_mahasiswa['id'])
        return render(request, 'mahasiswa/profile.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def rekomendasi(request):
    now = datetime.now()
    term_str = get_term(now)
    context_mahasiswa = get_context_mahasiswa(request, term_str)
    npm = context_mahasiswa['id']
    set_npm(npm)
    table = RekomendasiTable(get_recommendation(npm))
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    context_mahasiswa.update({'table': table})
    return render(request, 'mahasiswa/rekomendasi.tpl', context_mahasiswa)


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
