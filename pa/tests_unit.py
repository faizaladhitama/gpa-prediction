from django.test import TestCase


class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/pa', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_carimahasiswa(self):
        response = self.client.get('/pa/cari-mahasiswa', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/pa/profile', follow=True)
        self.assertEqual(response.status_code, 200)
