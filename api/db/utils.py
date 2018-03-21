from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester
from api.models import *
from random import randint

def getSiakData(npm, username, password):
    #kalo buat semuanya paling ITF , yang kita cuma bisa ambil 6 aja
    return get_academic_record(npm, username, password)

def parseSiakData(npm, username, password):
    data = getSiakData(npm, username, password)
    return data

def insertToDbRekamJejak(npm, kode_matkul, nilai, term=0):
    if Mahasiswa.objects.filter(npm=npm).count() < 1:
        createMahasiswa(npm=npm)
    if MataKuliah.objects.filter(kode_matkul=kode_matkul).count() < 1:
        createMataKuliah(kode_matkul=kode_matkul)
    npm = Mahasiswa.objects.get(npm=npm)
    kode_matkul = MataKuliah.objects.get(kode_matkul=kode_matkul)
    rj = RekamJejakNilaiMataKuliah(npm=npm, kode_matkul=kode_matkul, nilai=nilai, term=term)
    rj.save()

def createMahasiswa(npm, nama="nama_def", prodi="Tanpa Prodi", program="Tanpa Jenjang", nip_pa=""):
    if Dosen.objects.filter(nip=nip_pa).count() < 1:
        if nip_pa == "" :
            nip_pa = "1123456789" #default dosen
        #else:
        createDosen(nip=nip_pa, is_pa=True)

    m = Mahasiswa(npm=npm, nama=nama, study_program=prodi, educational_program=program)
    m.nip_pa = Dosen.objects.get(nip=nip_pa)
    m.save()

def createDosen(nip, nama="namadef", is_pa=False):
    d = Dosen(nama=nama, nip=nip, is_pa=is_pa)
    d.save()

def createMataKuliah(kode_matkul, nip=0, nama="namaMatkul", prodi="semua", tingkatKerjasama=1):
    matkul = MataKuliah(kode_matkul=kode_matkul, nip_pengajar=nip, nama_matkul=nama, prodi=prodi,
                        tingkatKerjasama=tingkatKerjasama)
    matkul.save()

def createMockDataMahasiswa():
    return True

def createMockDataDosen(jumlah):
    nama = "nama"
    is_pa = True
    for i in range(1, jumlah):
        namaCur = nama+str(i)
        nip = randint(100000000,999999999)
        dosen = Dosen(nama=namaCur, nip=str(nip), is_pa=is_pa)
        is_pa = True
        if randint(1,10) > 8:
            is_pa = False
        dosen.save()

#if __name__ == "__main__":
#   parseSiakData("1506722771", "muhammad.faiz52", "15kukusan")