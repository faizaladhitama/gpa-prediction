from django.core.management.base import BaseCommand
from api.ml_models.classifier import Classifier
from django.conf import settings

class Command(BaseCommand):
	args = '...'
	help = 'For Automaticaly train model'

	def add_arguments(self, parser):
		parser.add_argument('name', type=str, nargs='?', default="")

	def handle(self, *args, **options):
		print("Train prasyarat model")
		name = options.get('name', None)
		if name is not "":
			print("Name :",name)
			Classifier("final", md_name=name)
		else:
			Classifier("final")