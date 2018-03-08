from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class URLTest(TestCase):
	def test_login(self):
		response = self.client.get('login',follow=True)
		self.assertEqual(response.status_code, 200)

	def test_logout(self):
		response = self.client.get('logout',follow=True)
		self.assertEqual(response.status_code, 200)

