from django.test import TestCase
from selenium import webdriver

class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/mahasiswa', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_rekomendasi(self):
        response = self.client.get('/mahasiswa/rekomendasi', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/mahasiswa/profile', follow=True)
        self.assertEqual(response.status_code, 200)


class ElementTest(TestCase):

    def test_homepage(self):
        resp = self.client.get('/mahasiswa')
        self.assertNotContains(response=resp, text="<h10>", status_code=301)

    def test_search_bar(self):
        pass

    
            
