from django.test import TestCase

class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/dosen',follow=True)
        self.assertEqual(response.status_code, 200)

    def test_carimahasiswa(self):
        response = self.client.get('/dosen/cari-mahasiswa',follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/dosen/profile',follow=True)
        self.assertEqual(response.status_code, 200)