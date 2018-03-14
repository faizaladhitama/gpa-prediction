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
import django_cas_ng.views

from . import views

app_name = 'api'
CAS_LOGIN = django_cas_ng.views.login
CAS_LOGOUT = django_cas_ng.views.logout
urlpatterns = [
    url(r'^$', views.index, name='index'),
    re_path(r'^login$', views.login, name='login-page'),
    re_path(r'^auth-login$', views.auth_login, name='auth-login')
    #re_path(r'^login$', CAS_LOGIN, {"next_page": ""}, name='cas_ng_login'),
    #re_path(r'^logout$', CAS_LOGOUT, {"next_page": ""}, name='cas_ng_logout')
]
