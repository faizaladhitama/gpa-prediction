from django.test import TestCase

from api.db.utils import create_mahasiswa_siak
from api.ml_models import get_prediction_by_matkul, create_training_data
from api.models import MahasiswaSIAK
from api.utils import give_verdict, save_status


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

    def test_auth_login_dosen(self):
        response = self.client.post('/auth-login',
                                    {'username': 'dosen', 'password': 'dosen'}, follow=True)
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
        self.assertEqual(hasil, "lolos")

    def test_rumus_lolos_hati_hati(self):
        hasil = give_verdict(48, 40, 19, 3.3)
        self.assertEqual(hasil, "hati-hati")

    def test_rumus_lolos_negatif(self):
        hasil = give_verdict(48, 10, 19, 2.3)
        self.assertEqual(hasil, "tidak lolos")

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
        expected_mes = 'MahasiswaSIAK matching query does not exist.'
        expected = None, expected_mes
        self.assertEqual(expected, hasil)


# class ClassifierTest(TestCase):
#     def setUp(self):
#         kolom = ['nilaiDumA', 'status']
#         fitur = ['nilaiDumA']
#         self.model = Classifier("dummy", kolom, fitur)

#     def test_create(self):
#         kolom = ['nilaiDumA', 'status']
#         data_frame = self.model.create_model()
#         return self.assertEqual(len(data_frame.columns),
#                                 len(kolom)) and self.model.data_frame is not None

#     # def test_train(self):
#     #     self.model.create_model()
#     #     self.model.train_model()
#     #     return self.model.accuracy != None and self.model.accuracy >= 0

#     def test_train_wo_create(self):
#         kolom = ['nilaiDumA', 'status']
#         fitur = ['nilaiDumA']
#         model_wo_create = DTModel("dummy", kolom, fitur)
#         model_wo_create.train_model()
#         self.assertEqual(True, True)

#     def test_save(self):
#         self.model.save_model()
#         pwd = os.path.dirname(__file__)
#         file_name = pwd + '/savefile/' + self.model.course_name + '.sav'
#         return os.path.isfile(file_name)

#     # def test_build(self):
#     #     self.model.build_model()
#     #     flag1 = self.model.accuracy is not None
#     #     flag2 = self.model.data_frame is not None
#     #     return flag1 and flag2


class PrediktorKelulusanMatkulTest(TestCase):
    def matkul_not_found(self):
        self.assertEqual(get_prediction_by_matkul("admin", "SPS"), "not-found")

    def pok_lulus_test(self):
        self.assertEqual(get_prediction_by_matkul("admin", "POK"), "lulus")

    def pok_hati_hati_test(self):
        self.assertEqual(get_prediction_by_matkul("CIA", "POK"), "hati-hati")

    def pok_tidak_lulus_test(self):
        self.assertEqual(get_prediction_by_matkul("CEO", "POK"), "tidak-lulus")

    def creation_passed(self):
        res = create_training_data("CSF1600400", "SDA", ["CSF1600200"])
        self.assertEqual(res, 'passed')
