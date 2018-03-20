from django.test import TestCase


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
    def function(self):
        resp = self.client.get('/mahasiswa')
        #with self.assertHTML(resp) as html:
        #     self.assertNotEqual(html.find('body/h10').text, '') , unknown error
