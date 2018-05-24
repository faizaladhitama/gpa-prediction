from django.db import models
# Create your models here.
class Civitas(models.Model):
    nama = models.TextField(max_length=100, blank=True)

class Mahasiswa(Civitas):
    npm = models.TextField(primary_key=True, max_length=100, blank=True)
    study_program = models.TextField(max_length=100, blank=True)
    nip_pa = models.ForeignKey('Dosen', on_delete=models.CASCADE)

class MahasiswaSIAK(Mahasiswa):
    status_evaluasi = models.TextField()

class MahasiswaSSO(Mahasiswa):
    ldap_cn = models.TextField(max_length=100, blank=True)
    kd_org = models.TextField(max_length=100, blank=True)
    faculty = models.TextField(max_length=100, blank=True)

class MataKuliah(models.Model):
    kode_matkul = models.TextField(primary_key=True, max_length=100, blank=True) # key
    nip_pengajar = models.IntegerField()
    sks = models.IntegerField()
    nama_matkul = models.CharField(max_length=40)
    prodi = models.CharField(max_length=30)
    tingkatKerjasama = models.IntegerField(0)

class Dosen(Civitas):
    nip = models.TextField(primary_key=True, max_length=100, blank=True)
    is_pa = models.BooleanField()

class AnggotaKelas(models.Model):
    npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
    kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)

class PrasyaratMataKuliah(models.Model):
    kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)
    nama_matkul = models.CharField(max_length=100, null=True)
    kode_matkul_pras = models.CharField(max_length=100)
    nama_matkul_pras = models.CharField(max_length=150, null=True)

class InformasiAkademis(models.Model):
    npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
    ip = models.IntegerField()
    sks_dipunya = models.IntegerField()

class PrediksiMataKuliah(models.Model):
    npm = models.ForeignKey('MahasiswaSIAK', on_delete=models.CASCADE)
    kode_matkul = models.TextField(primary_key=True, max_length=100, blank=True)
    status = models.TextField()

class RekamJejakNilaiMataKuliah(models.Model):
    npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
    kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)
    nilai = models.CharField(max_length=2)
    term = models.IntegerField()
