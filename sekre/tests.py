from django.test import TestCase

class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_carimahasiswa(self):
        response = self.client.get('/cari-mahasiswa')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)