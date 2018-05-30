from django.core.management.base import BaseCommand
from api.models import Mahasiswa, MataKuliah, Dosen
from api.db.utils import populate_prasyarat_matkul
from django.conf import settings

class Command(BaseCommand):
	args = '...'
	help = 'For Automaticaly populate DB with randomized value , Populate Mahasiswa , Matkul, and Dosen'

	def _create_mahasiswa(self):
		m1 = Mahasiswa()

	def handle(self, *args, **options):
		print("Populate prasyarat matkul")
		populate_prasyarat_matkul(settings.BASE_DIR + "/api/db/prasyarat_matkul.csv")