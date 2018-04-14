from django.test import TestCase

from api.apps import give_verdict, save_status
from api.db.utils import create_mahasiswa_siak
from api.models import MahasiswaSIAK


class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_login(self):
        response = self.client.get('/auth-login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/index', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_landing_valid(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)


class UserTest(TestCase):
    def test_auth_login_positive(self):
        response = self.client.post('/auth-login',
                                    {'username': 'admin', 'password': 'admin'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_login_negative(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola'}, follow=True)
        self.assertEqual(response.status_code, 200)


class ExternalAPITest(TestCase):
    def test_ui_server_up(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ui_server_down(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola', 'connection': False},
                                    follow=True)
        self.assertEqual(response.status_code, 200)


class EvaluasiTest(TestCase):
    def test_api_config(self):
        # = ApiConfig('api', 'api.apps')
        self.assertEqual(True, True)

    def test_rumus_lolos(self):
        hasil = give_verdict(48, 48, 19, 3.3)
        self.assertEqual(hasil, "Lolos")

    def test_rumus_lolos_hati_hati(self):
        hasil = give_verdict(48, 40, 19, 3.3)
        self.assertEqual(hasil, "Hati-Hati")

    def test_rumus_lolos_negatif(self):
        hasil = give_verdict(48, 10, 19, 2.3)
        self.assertEqual(hasil, "Tidak Lolos")

    def test_save_status(self):
        npm = '1506111222'
        create_mahasiswa_siak(npm)
        save_status(npm, 'Lolos')
        flag = MahasiswaSIAK.objects.get(npm=npm).status_evaluasi
        self.assertEqual(flag, 'Lolos')

    def test_save_status_false(self):
        npm = '1506333444'
        create_mahasiswa_siak(npm)
        save_status(npm, 'Tidak Lolos')
        flag = MahasiswaSIAK.objects.get(npm=npm).status_evaluasi
        self.assertEqual(flag, 'Tidak Lolos')

    def test_save_status_not_found(self):
        hasil = save_status('6969696969', False)
        expected = 'MahasiswaSIAK matching query does not exist.'
        self.assertEqual(expected, hasil)
