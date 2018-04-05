from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

def __init__():
    pass

def give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_sekarang):
    status = "Tidak Lolos"
    sks_kemungkinan = sks_lulus + sks_diambil
    ip_aman = ip_sekarang >= 2
    if(ip_aman and sks_lulus >= sks_minimal):
        status = "Lolos"
    elif(ip_aman and sks_lulus < sks_minimal and sks_kemungkinan >= sks_minimal):
        status = "Hati Hati"
    return status
