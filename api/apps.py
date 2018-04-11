from django.apps import AppConfig
from api.models import Dosen, Mahasiswa, RekamJejakNilaiMataKuliah, MataKuliah

class ApiConfig(AppConfig):
    name = 'api'

def give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_sekarang):
    status = "Tidak Lolos"
    sks_kemungkinan = sks_lulus + sks_diambil
    ip_aman = ip_sekarang >= 2
    if(ip_aman and sks_lulus >= sks_minimal):
        status = "Lolos"
    elif(ip_aman and sks_lulus < sks_minimal and sks_kemungkinan >= sks_minimal):
        status = "Hati-Hati"
    return status

def save_status(npm, status):
    try:
        mahasiswa = Mahasiswa.objects.get(npm = npm)
        mahasiswa.status_evaluasi = status
        mahasiswa.save()
    except:
        print("Exceptions Happened at save_status") 
