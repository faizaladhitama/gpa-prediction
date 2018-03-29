from unittest.mock import patch
from django.test import TestCase
import pandas as pd
import os.path
from models.nb_model import NbModel

class NbModelTest(TestCase):
	def setUp(self):
		kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
		fitur = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP',]
		self.model = NbModel("dummy", kolom, fitur)
	
	def test_create(self):
		kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
		df = self.model.create_model()
		assertEqual(len(df.columns,len(kolom)))

	def test_train(self):
		self.model.train_model()
		return self.accuracy != None and self.accuracy >= 0

	def test_save(self):
		self.model.save_model()
		pwd = os.path.dirname(__file__)
		file_name = pwd+'/savefile/'+self.course_name+'.sav'
		return os.path.isfile(fn)

	def test_build(Self):
		self.model.build_model()
		flag1 = self.accuracy != None
		flag2 = self.df != None
		return flag1 and flag2

	def tearDown(self):
		pwd = os.path.dirname(__file__)
		file_name = pwd+'/savefile/'+self.course_name+'.sav'
		os.remove(file_name)