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

from . import views

app_name = 'mahasiswa'
urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^rekomendasi$', views.rekomendasi, name='rekomendasi'),
    url(r'^prediktor-matkul$', views.prediktor_matkul, name='prediktor-matkul'),
=======
    url(r'^prediktor-matkul$', views.prediktor_matkul, name='prediktor-matkul')
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
]
