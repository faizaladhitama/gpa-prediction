from django.test import TestCase
from unittest.mock import Mock, patch
from api.prediction import Predictor, predict_matkul
import pickle
import pandas as pd
import numpy as np
import os.path

class PredictorTest(TestCase):
	def setUp(self):
		self.predictor = Predictor()

	def test_set_prediction(self):
		self.predictor.set_prediction("matakuliah")

		self.assertEqual("matakuliah", self.predictor.prediction)

	def test_set_data(self):
		pwd = os.path.dirname(__file__)
		mocked_data = pd.read_csv(pwd + "/mock/data.csv", header=None, delimiter=",", engine='python')
		self.predictor.set_data(mocked_data)

		self.assertIsNotNone(self.predictor.data)

	def test_load_model_on_valid(self):
		self.predictor.load_model("dummy")
		self.assertIsNotNone(self.predictor.model)

	def test_load_model_on_invalid(self):
		self.predictor.load_model("kafuu chino")
		self.assertIsNone(self.predictor.model)

	def test_check_none(self):
		self.predictor.prediction = None

		with self.assertRaises(Exception) as context:
			self.predictor.check_none()

		self.assertTrue("is None" in str(context.exception))

		self.predictor.prediction = "mocked"
		self.predictor.data = None

		with self.assertRaises(Exception) as context:
			self.predictor.check_none()

		self.assertTrue("is None" in str(context.exception))

		self.predictor.data = "mocked"
		self.predictor.model = None

		with self.assertRaises(Exception) as context:
			self.predictor.check_none()

		self.assertTrue("is None" in str(context.exception))

	@patch("api.prediction.Predictor.check_none")
	def test_predict_on_valid(self, mocked_check):
		self.predictor.prediction = "matakuliah"
		self.predictor.data = np.array([[1,0,1,2,2]])
		self.predictor.load_model("pok")

		res, err = self.predictor.predict()
		self.assertIsNone(err)
		self.assertIsNotNone(res)

	@patch("api.prediction.Predictor.check_none")
	def test_predict_on_invalid(self, mocked_check):
		self.predictor.prediction = "mocked"

		res, err = self.predictor.predict()
		self.assertIsNone(res)
		self.assertEqual("prediction is not define", err)

	@patch("api.prediction.Predictor.check_none")
	def test_predict_on_type_error(self, mocked_check):
		mocked_check.side_effect = TypeError("mocked error")
		
		res, err = self.predictor.predict()

		self.assertIsNone(res)
		self.assertEqual("mocked error", err)

class InitTest(TestCase):

	@patch("api.prediction.Predictor")
	def test_predict_matkul(self, mocked):
		mocked_predictor = mocked.return_value
		mocked_predictor.predict.return_value = (12, None)
		res, err = predict_matkul("mocked", "mocked")

		self.assertIsNone(err)
		self.assertIsInstance(res, int)




