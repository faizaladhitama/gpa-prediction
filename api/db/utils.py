from random import randint
import json

from django.core.cache import cache, caches
from django.core.cache.backends.base import InvalidCacheBackendError

from api.models import Dosen, Mahasiswa, RekamJejakNilaiMataKuliah, MataKuliah,\
 MahasiswaSIAK


def insert_to_db_rekam_jejak(npm, kode_matkul, nilai, term=0):
    if Mahasiswa.objects.filter(npm=npm).count() < 1:
        create_mahasiswa(npm=npm)
    if MataKuliah.objects.filter(kode_matkul=kode_matkul).count() < 1:
        create_matakuliah(kode_matkul=kode_matkul)
    npm = Mahasiswa.objects.get(npm=npm)
    kode_matkul = MataKuliah.objects.get(kode_matkul=kode_matkul)
    rj_new = RekamJejakNilaiMataKuliah(npm=npm, kode_matkul=kode_matkul, nilai=nilai, term=term)
    rj_new.save()

def create_mahasiswa(npm, nama="nama_def", prodi="Tanpa Prodi", nip_pa=""):
    if Dosen.objects.filter(nip=nip_pa).count() < 1:
        if nip_pa == "":
            nip_pa = "1123456789"  # default dosen
        # else:
        create_dosen(nip=nip_pa, is_pa=True)

    ma_new = Mahasiswa(npm=npm, nama=nama, study_program=prodi)
    ma_new.nip_pa = Dosen.objects.get(nip=nip_pa)
    ma_new.save()


def create_mahasiswa_siak(npm, nama="nama_def", prodi="no Prodi", nip_pa=""):
    if Dosen.objects.filter(nip=nip_pa).count() < 1:
        if nip_pa == "":
            nip_pa = "1234567890"  # default dosen
        # else:
        create_dosen(nip=nip_pa, is_pa=True)

    ma_new = MahasiswaSIAK(npm=npm, nama=nama, study_program=prodi)
    ma_new.status_evaluasi = False
    ma_new.nip_pa = Dosen.objects.get(nip=nip_pa)
    ma_new.save()

def create_dosen(nip, nama="namadef", is_pa=False):
    do_new = Dosen(nama=nama, nip=nip, is_pa=is_pa)
    do_new.save()

def create_matakuliah(kode_matkul, nip=0, nama="namaMatkul", prodi="semua", tkt_krjsama=1, sks=3):
    matkul = MataKuliah(kode_matkul=kode_matkul, nip_pengajar=nip, nama_matkul=nama, prodi=prodi,
                        tingkatKerjasama=tkt_krjsama, sks=sks)
    matkul.save()

 # def insert_to_db_matakuliah(kode_matkul, nama):
 #    pass

def create_mock_data_mahasiswa():
    return True


def create_mock_data_dosen(jumlah):
    nama = "nama"
    is_pa = True
    for i in range(1, jumlah):
        nama_cur = nama + str(i)
        nip = randint(100000000, 999999999)
        dosen = Dosen(nama=nama_cur, nip=str(nip), is_pa=is_pa)
        is_pa = True
        dosen.save()


def caching(name, func, args, kode=""):
    name = kode + "_" + name
    try:
        if cache.get(name) is None:
            if isinstance(args, tuple):
                temp = func(*args)
                if isinstance(temp, dict):
                    raise TypeError
                ret, err = temp
            else:
                res = func(args)
                if isinstance(res, (str, dict)):
                    raise TypeError
                ret, err = res
            cache.set(name, (ret, err))
        else:
            ret, err = cache.get(name)
            print("use cache w err " + name)
        return ret, err
    except (TypeError, ValueError):
        if cache.get(name) is None:
            if isinstance(args, tuple):
                ret = func(*args)
            else:
                ret = func(args)
            if isinstance(ret, dict):
                cache.set(name, json.dumps(ret))
            else:
                cache.set(name, ret)
        else:
            try:
                ret = json.loads(caches[name])
            except InvalidCacheBackendError:
                ret = cache.get(name)
            print("use cache " + name)
        #handle tuple object (dict, _)
        if isinstance(ret, str) and ret[0] == "{":
            ret = json.loads(ret)
        return ret
