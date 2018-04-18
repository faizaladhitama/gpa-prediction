from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist
from api.models import MahasiswaSIAK

class ApiConfig(AppConfig):
    name = 'api'

def give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_sekarang):
    status = "Tidak Lolos"
    sks_kemungkinan = sks_lulus + sks_diambil
    ip_aman = ip_sekarang >= 2.0
    if(ip_aman and sks_lulus >= sks_minimal):
        status = "Lolos"
    elif(ip_aman and sks_lulus < sks_minimal and sks_kemungkinan >= sks_minimal):
        status = "Hati-Hati"
    return status

def save_status(npm, status):
    try:
        mahasiswa = MahasiswaSIAK.objects.get(npm=npm)
        mahasiswa.status_evaluasi = status
        mahasiswa.save()
        return status
    except ObjectDoesNotExist as exception:
        return None, str(exception)
