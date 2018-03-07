from django.db import models

# Create your models here.
class Mahasiswa(models.Model):

	npm = models.IntegerField()
	angkatan = models.IntegerField()
	nama = models.CharField(max_length = 20)

class Matakuliah(models.Model):

	kode_matkul = models.IntegerField()
	nip_pengajar = models.IntegerField()