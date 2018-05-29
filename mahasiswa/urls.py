"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'mahasiswa'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^rekomendasi$', views.rekomendasi, name='rekomendasi'),
    url(r'^peraturan-akademik$', views.peraturan_akademik, name='peraturan_akademik'),
    url(r'^riwayat-ip$', views.riwayat_ip, name='riwayat_ip'),
    url(r'^riwayat-sks$', views.riwayat_sks, name='riwayat_sks'),
    url(r'^prediktor-matkul$', views.prediktor_matkul, name='prediktor_matkul'),
    url(r'^search-matkul$', views.search_matkul, name='search_matkul'),
    re_path(r'^query-checker$', views.query_checker, name='query-checker'),
]
