from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/mahasiswa/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_rekomendasi(self):
        response = self.client.get('/mahasiswa/rekomendasi', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/mahasiswa/profile', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_prediktor_evaluasi(self):
        response = self.client.get('/mahasiswa/prediktor_evaluasi', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_prediktor_matkul_url_is_exist(self):
        response = self.client.get('/prediktor-matkul', follow=True)
        self.assertEqual(response.status_code, 200)


class ElementTest(TestCase):
    def test(self):
        return True
