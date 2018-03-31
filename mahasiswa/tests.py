from django.test import TestCase


class PrediktorKelulusanMatkulTest(TestCase):
    def test_prediktor_matkul_url_exist(self):
        response = self.client.post('/mahasiswa/prediktor-matkul', follow=True)
        self.assertEqual(response.status_code, 200)
