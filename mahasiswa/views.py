import time
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from api.db.utils import caching
from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_index_mahasiswa_context, get_riwayat_sks, get_riwayat_ip, \
    get_peraturan, get_profile, get_prediktor_matkul_context


# Create your views here.


def index(request):
    #start = time.time()
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
        # context_mahasiswa = get_context_mahasiswa(request, term_str)
        # index_context = get_index_mahasiswa_context(request,
        #                                             context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        index_context = caching("get_index_mahasiswa",
                                get_index_mahasiswa_context,
                                (request, context_mahasiswa),
                                context_mahasiswa['id'])
        return render(request, 'mahasiswa/index.tpl', index_context)
    except TypeError as err_msg:
        print('ini eror' + str(err_msg))
        return render(request, 'landing_page.tpl', {})


def prediktor_matkul(request):
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
        #context_mahasiswa = get_context_mahasiswa(request, term_str)
        # prediktor_matkul_context = get_prediktor_matkul_context(request,
        #                                                         'Jejaring Semantik',
        #                                                         context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        # prediktor_matkul_context = caching("get_prediktor_matkul_context",
        #                                    get_prediktor_matkul_context,
        #                                    (request, 'Analisis Numerik',
        #                                     context_mahasiswa), context_mahasiswa['id'])
        print("CONTEXT ON Analisis")
        print(request.session['matkul-predict'])
        prediktor_matkul_context = get_prediktor_matkul_context(request,\
         request.session['matkul-predict'], context_mahasiswa)
        print("CONTEXT ON predictor_matkul " + str(prediktor_matkul_context))
        return render(request, 'mahasiswa/prediktor-matkul.tpl', prediktor_matkul_context)
    except TypeError as err_msg:
        print('ini eror' + str(err_msg))
        return render(request, 'landing_page.tpl', {})

def search_matkul(request):
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
        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        return render(request, 'search-bar.tpl', context_mahasiswa)
    except TypeError:
        return render(request, 'landing_page.tpl', {})

def query_checker(request):
    matkul_to_predict = request.POST['matkul']
    request.session['matkul-predict'] = matkul_to_predict
    return HttpResponseRedirect(reverse('mahasiswa:prediktor_matkul'))


def profile(request):
    start = time.time()
    now = datetime.now()
    term_str = get_term(now)
    try:
        # context_mahasiswa = get_context_mahasiswa(request, term_str)
        # context = get_profile(request, context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        context = caching("get_profile", get_profile, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        print("Time :", time.time() - start)
        return render(request, 'mahasiswa/profile.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def rekomendasi(request):
    context = {'name': 'mahasiswa'}
    return render(request, 'mahasiswa/rekomendasi.tpl', context)


def riwayat_sks(request):
    start = time.time()
    now = datetime.now()
    term_str = get_term(now)
    try:
        # context_mahasiswa = get_context_mahasiswa(request, term_str)
        # context = get_riwayat_sks(request, context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        context = caching("get_riwayat_sks", get_riwayat_sks, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        print("Time :", time.time() - start)
        return render(request, 'mahasiswa/sks-term-table.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def riwayat_ip(request):
    start = time.time()
    now = datetime.now()
    term_str = get_term(now)
    try:
        # context_mahasiswa = get_context_mahasiswa(request, term_str)
        # context = get_riwayat_ip(request, context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        context = caching("get_riwayat_ip", get_riwayat_ip, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        print("Time :", time.time() - start)
        return render(request, 'mahasiswa/graph-ip_term.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})


def peraturan_akademik(request):
    start = time.time()
    now = datetime.now()
    term_str = get_term(now)
    try:
        # context_mahasiswa = get_context_mahasiswa(request, term_str)
        # context = get_peraturan(request, context_mahasiswa)

        context_mahasiswa = caching("get_context_mahasiswa", get_context_mahasiswa,
                                    (request, term_str), request.session['kode_identitas'])
        context = caching("get_peraturan", get_peraturan, (request, context_mahasiswa),
                          context_mahasiswa['id'])
        print("Time :", time.time() - start)
        return render(request, 'mahasiswa/peraturan-akademik.tpl', context)
    except TypeError:
        return render(request, 'landing_page.tpl', {})
