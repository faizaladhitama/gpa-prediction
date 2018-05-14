from django.core.management.base import BaseCommand
from api.models import Mahasiswa, MataKuliah, Dosen

class Command(BaseCommand):
	args = '...'
	help = 'For Automaticaly populate DB with randomized value , Populate Mahasiswa , Matkul, and Dosen'

	def _create_mahasiswa(self):
		m1 = Mahasiswa()