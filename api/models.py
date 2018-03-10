from django.db import models

# Create your models here.
class Mahasiswa(models.Model):

	npm = models.IntegerField(primary_key=True) #key
	angkatan = models.IntegerField()
	prodi = models.CharField(max_length = 20)
	nama = models.CharField(max_length = 100)
	status_evaluasi = models.BooleanField()

class MataKuliah(models.Model):

	kode_matkul = models.IntegerField(primary_key=True) # key
	nip_pengajar = models.IntegerField()
	nama_matkul = models.CharField(max_length = 40)
	prodi = models.CharField(max_length = 30)
	tingkatKerjasama = models.IntegerField(0)

class Dosen(models.Model):
	nip_pengajar = models.IntegerField(primary_key=True)
	nama_dosen = models.CharField(max_length = 100)
	is_pa = models.BooleanField()

class AnggotaKelas(models.Model):
	npm = models.IntegerField()
	kode_matkul = models.IntegerField()

class PrasyaratMataKuliah:
    kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)
    kode_matkul_pras = models.CharField()

class InformasiAkademis:
	npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	ip = models.IntegerField()
	sks_dipunya = models.IntegerField()

class PrediksiMataKuliah:
	npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)

class RekamJejakNilaiMataKuliah:
	npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)
	nilai = models.IntegerField()
	Term = models.IntegerField()