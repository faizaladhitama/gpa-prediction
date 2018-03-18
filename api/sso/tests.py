from django.test import TestCase
from . import SSOClient
import requests

class SSOTestCase(TestCase):
	def setUpTestData(self):
		self.user = {'username': 'mocked','password': '23419123j1312'}

	def test_token_in_success(self):
		client = SSSOClient(self.user)
		self.assertEqual(client.generate_token(), )



