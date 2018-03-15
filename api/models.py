import json
import os
from backend.settings import BASE_DIR
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Civitas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peran_user = models.TextField(max_length=100, blank=True)
    nama = models.TextField(max_length=100, blank=True)

class Staff(Civitas):
    nip = models.TextField(max_length=100, blank=True)

class Mahasiswa(Civitas):
    npm = models.TextField(primary_key=True, max_length=100, blank=True)
    study_program = models.TextField(max_length=100, blank=True)
    educational_program = models.TextField(max_length=100, blank=True)
    nip_pa = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)

class MahasiswaSIAK(Mahasiswa):
	status_evaluasi = models.BooleanField()

class MahasiswaSSO(Mahasiswa):
    ldap_cn = models.TextField(max_length=100, blank=True)
    kd_org = models.TextField(max_length=100, blank=True)
    faculty = models.TextField(max_length=100, blank=True)

class MataKuliah(models.Model):

	kode_matkul = models.TextField(primary_key=True, max_length=100, blank=True) # key
	nip_pengajar = models.IntegerField()
	nama_matkul = models.CharField(max_length = 40)
	prodi = models.CharField(max_length = 30)
	tingkatKerjasama = models.IntegerField(0)

class Dosen(models.Model):
	nip_pengajar = models.IntegerField(primary_key=True)
	nama_dosen = models.CharField(max_length = 100)
	is_pa = models.BooleanField()

class AnggotaKelas(models.Model):
	npm = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	kode_matkul = models.ForeignKey('MataKuliah', on_delete=models.CASCADE)

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


def create_user_profile(instance, created, **kwargs):
    print("create")
    if created:
        print("created")
        print(kwargs)
        attributes = kwargs.get('attributes', [])
        nama = attributes['nama']
        peran = attributes['peran_user']
        if peran == "mahasiswa":
            kd_org = attributes['kd_org']
            npm = attributes['npm']
            ldap_cn = attributes['ldap_cn']
            path = os.path.join(BASE_DIR, './static/additional-info.json')
            with open(path) as file:
                data = json.loads(file.read())[kd_org]
                faculty = data['faculty']
                study_prog = data['study_program']
                educational_prog = data['educational_program']
                print(faculty, study_prog, educational_prog)
            mahasiswa_length = len(list(Mahasiswa.objects.filter(npm=npm)))
            if mahasiswa_length == 0:
                print("create profile")
                print(attributes)
                mahasiswa = Mahasiswa.objects
                mahasiswa.create(user=instance, ldap_cn=ldap_cn, kd_org=kd_org,
                                 peran_user=peran, nama=nama, npm=npm, faculty=faculty,
                                 study_program=study_prog, educational_program=educational_prog)
        elif peran == "staff":
            nip = attributes['nip']
            staff_length = len(list(Staff.objects.filter(nip=nip)))
            if staff_length == 0:
                print("create profile")
                print(attributes)
                Staff.objects.create(user=instance, nip=nip)