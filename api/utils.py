from django.core.exceptions import ObjectDoesNotExist

from api.models import MahasiswaSIAK, PrediksiMataKuliah
from api.db.utils import create_mahasiswa_siak

def give_verdict(sks_minimal, sks_lulus, sks_diambil, ip_sekarang):
    status = "Tidak Lolos"
    sks_kemungkinan = sks_lulus + sks_diambil
    ip_aman = ip_sekarang >= 2.0
    if (ip_aman and sks_lulus >= sks_minimal):
        status = "Lolos"
    elif (ip_aman and sks_lulus < sks_minimal and sks_kemungkinan >= sks_minimal):
        status = "Hati-Hati"
    return status.lower()


def save_status(npm, status):
    try:
        mahasiswa = MahasiswaSIAK.objects.get(npm=npm)
        mahasiswa.status_evaluasi = status
        mahasiswa.save()
        return status
    except ObjectDoesNotExist as exception:
        return None, str(exception)

def save_status_matakuliah(npm, kd_mk, status):
    try:
        if MahasiswaSIAK.objects.filter(npm=npm).count() < 1:
            create_mahasiswa_siak(npm)
        mahasiswa = MahasiswaSIAK.objects.get(npm=npm)
        record = PrediksiMataKuliah(mahasiswa, kd_mk, status)
        record.save()
        return status
    except ObjectDoesNotExist as exception:
        return None, str(exception)
