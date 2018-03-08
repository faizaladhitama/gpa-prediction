from django.db import models
from django.contrib.auth.models import User
from django_cas_ng.signals import cas_user_authenticated
import os
from backend.settings import BASE_DIR
import json

class Civitas(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	peran_user = models.TextField(max_length=100, blank=True)
	nama = models.TextField(max_length=100, blank=True)

class Staff(Civitas):
	nip = models.TextField(max_length=100, blank=True)

class Mahasiswa(Civitas):
	ldap_cn = models.TextField(max_length=100, blank=True)
	kd_org = models.TextField(max_length=100, blank=True)
	npm = models.TextField(max_length=100, blank=True)
	faculty = models.TextField(max_length=100, blank=True)
	study_program = models.TextField(max_length=100, blank=True)
	educational_program = models.TextField(max_length=100, blank=True)

def create_user_profile(instance, created, **kwargs):
	print("create")
	if created:
		print("created")
		print(kwargs)
		attributes = kwargs.get('attributes',[])
		nama = attributes['nama']
		peran_user = attributes['peran_user']
		if peran_user == "mahasiswa":
			kd_org = attributes['kd_org']
			npm = attributes['npm']	
			ldap_cn = attributes['ldap_cn']
			path = os.path.join(BASE_DIR, './static/additional-info.json')			
			with open(path) as f:
				data = json.loads(f.read())[kd_org]
				faculty = data['faculty']
				study_program = data['study_program']
				educational_program = data['educational_program']
				print(faculty,study_program,educational_program)
			if len(list(Mahasiswa.objects.filter(npm=npm))) == 0:
				print("create profile")
				print(attributes)
				Mahasiswa.objects.create(user=instance,ldap_cn=ldap_cn,kd_org=kd_org,
					peran_user=peran_user,nama=nama,npm=npm,faculty=faculty,
					study_program=study_program,educational_program=educational_program)
		elif peran_user == "staff":
			nip = attributes['nip']	
			if len(list(Staff.objects.filter(nip=nip))) == 0:
				print("create profile")
				print(attributes)
				Staff.objects.create(user=instance,nip=nip)			