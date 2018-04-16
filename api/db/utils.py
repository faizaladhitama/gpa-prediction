from random import randint
from api.siak import get_academic_record
from api.models import Dosen, Mahasiswa, RekamJejakNilaiMataKuliah, MataKuliah, MahasiswaSIAK

def get_siak_data(npm, username, password):
    #kalo buat semuanya paling ITF , yang kita cuma bisa ambil 6 aja
    return get_academic_record(npm, username, password)

def parse_siak_data(npm, username, password):
    data = get_siak_data(npm, username, password)
    return data

def insert_to_db_rekam_jejak(npm, kode_matkul, nilai, term=0):
    if Mahasiswa.objects.filter(npm=npm).count() < 1:
        create_mahasiswa(npm=npm)
    if MataKuliah.objects.filter(kode_matkul=kode_matkul).count() < 1:
        create_matakuliah(kode_matkul=kode_matkul)
    npm = Mahasiswa.objects.get(npm=npm)
    kode_matkul = MataKuliah.objects.get(kode_matkul=kode_matkul)
    rj_new = RekamJejakNilaiMataKuliah(npm=npm, kode_matkul=kode_matkul, nilai=nilai, term=term)
    rj_new.save()

def create_mahasiswa(npm, nama="nama_def", prodi="Tanpa Prodi", program="Tanpa Jenjang", nip_pa=""):
    if Dosen.objects.filter(nip=nip_pa).count() < 1:
        if nip_pa == "":
            nip_pa = "1123456789" #default dosen
        #else:
        create_dosen(nip=nip_pa, is_pa=True)

    ma_new = Mahasiswa(npm=npm, nama=nama, study_program=prodi, educational_program=program)
    ma_new.nip_pa = Dosen.objects.get(nip=nip_pa)
    ma_new.save()

def create_mahasiswa_siak(npm, nama="nama_def", prodi="no Prodi", program="no Jenjang", nip_pa=""):
    if Dosen.objects.filter(nip=nip_pa).count() < 1:
        if nip_pa == "":
            nip_pa = "1234567890" #default dosen
        #else:
        create_dosen(nip=nip_pa, is_pa=True)

    ma_new = MahasiswaSIAK(npm=npm, nama=nama, study_program=prodi, educational_program=program)
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

def create_mock_data_mahasiswa():
    return True

def create_mock_data_dosen(jumlah):
    nama = "nama"
    is_pa = True
    for i in range(1, jumlah):
        nama_cur = nama+str(i)
        nip = randint(100000000, 999999999)
        dosen = Dosen(nama=nama_cur, nip=str(nip), is_pa=is_pa)
        is_pa = True
        dosen.save()