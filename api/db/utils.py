from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester
from api.models import *
from random import randint

def getSiakData(npm, username, password):
	#kalo buat semuanya paling ITF , yang kita cuma bisa ambil 6 aja
	res = get_academic_record(npm, username, password)
	return res
	
def parseSiakData(npm, username, password):
	data = getSiakData(npm, username, password)
	return "ABC"

def insertToDbRekamJejak(npm, kode_matkul, nilai):
	if(Mahasiswa.objects.filter(npm=npm).count() < 1):
		createMahasiswa(npm=npm)
	if(MataKuliah.objects.filter(kode_matkul=kode_matkul).count() < 1):
		createMataKuliah(kode_matkul=kode_matkul)
	rj = RekamJejakNilaiMatakuliah(npm=npm, kode_matkul=kode_matkul, nilai=nilai)
	rj.save()

def createMahasiswa(npm, nama="nama_def", prodi="Tanpa Prodi", program="Tanpa Jenjang", nip_pa=""):		
	if(Dosen.objects.filter(nip=nip_pa).count() < 1):
		if(nip_pa==""):
			nip_pa="123456789" #default dosen
		else:
			createDosen(nip=nip_pa,is_pa=True)

	m = Mahasiswa(npm=npm, nama=nama, study_program=prodi, educational_program=program)
	m.nip_pa = nip_pa
	m.save()

def createDosen(nama, nip, is_pa=False):
	d = Dosen(nama="namaDef", nip=nip, is_pa=is_pa)
	d.save()

def createMockDataMahasiswa(self):
	pass

def createMockDataDosen(jumlah):
	nama = "nama"
	is_pa = True
	for i in range(1,jumlah):
		namaCur=nama+str(i)
		nip=randint(100000000,999999999)
		dosen = Dosen(nama=namaCur, nip=str(nip), is_pa=is_pa)
		is_pa = True
		if(randint(1,10) > 8):
			is_pa = False
		dosen.save()
