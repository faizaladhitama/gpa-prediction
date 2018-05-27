import os.path

from django.test import TestCase

from api.ml_models.dt_model import DTModel
from api.ml_models.nb_model import NbModel


class NbModelTest(TestCase):
    def setUp(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        fitur = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP']
        self.model = NbModel("dummy", kolom, fitur)

    def test_create(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        data_frame = self.model.create_model()
        return self.assertEqual(len(data_frame.columns),
                                len(kolom)) and self.model.data_frame is not None

    def test_train(self):
        self.model.create_model()
        self.model.train_model()
        return self.model.accuracy != None and self.model.accuracy >= 0

    def test_train_wo_create(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        fitur = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP']
        model_wo_create = NbModel("dummy", kolom, fitur)
        model_wo_create.train_model()
        self.assertEqual(True, True)

    def test_save(self):
        self.model.save_model()
        pwd = os.path.dirname(__file__)
        file_name = pwd + '/savefile/' + self.model.course_name + '.sav'
        self.assertTrue(os.path.isfile(file_name))

    def test_build(self):
        self.model.build_model()
        flag1 = self.model.accuracy is not None
        flag2 = self.model.data_frame is not None
        self.assertTrue(flag1)
        self.assertTrue(flag2)


class DTModelTest(TestCase):
    def setUp(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        fitur = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP']
        self.model = DTModel("dummy", kolom, fitur)

    def test_create(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        data_frame = self.model.create_model()
        return self.assertEqual(len(data_frame.columns),
                                len(kolom)) and self.model.data_frame is not None

    def test_train(self):
        self.model.create_model()
        self.model.train_model()
        return self.model.accuracy != None and self.model.accuracy >= 0

    def test_train_wo_create(self):
        kolom = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP', 'status']
        fitur = ['nilaiDumA', 'nilaiDumB', 'absDumA', 'absDumB', 'IP']
        model_wo_create = DTModel("dummy", kolom, fitur)
        model_wo_create.train_model()
        self.assertEqual(True, True)

    def test_save(self):
        self.model.save_model()
        pwd = os.path.dirname(__file__)
        file_name = pwd + '/savefile/' + self.model.course_name + '.sav'
        return os.path.isfile(file_name)

    def test_build(self):
        self.model.build_model()
        flag1 = self.model.accuracy is not None
        flag2 = self.model.data_frame is not None
        return flag1 and flag2


class PrediktorKelulusanMatkulTest(TestCase):
    def matkul_not_found(self):
        # self.assertEqual(get_prediction_by_matkul("admin", "SPS"), "not-found")
        pass

    def pok_lulus_test(self):
        # self.assertEqual(get_prediction_by_matkul("admin", "POK"), "lulus")
        pass

    def pok_hati_hati_test(self):
        # self.assertEqual(get_prediction_by_matkul("CIA", "POK"), "hati-hati")
        pass

    def pok_tidak_lulus_test(self):
        # self.assertEqual(get_prediction_by_matkul("CEO", "POK"), "tidak-lulus")
        pass

    def creation_passed(self):
        # res = create_training_data("CSF1600400", "SDA", ["CSF1600200"])
        # self.assertEqual(res, 'passed')
        pass
