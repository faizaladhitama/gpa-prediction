from django.test import TestCase
import numpy as np

from api.ml_models import get_prediction, \
    huruf_converter, huruf_status_converter, create_training_data
from api.ml_models.classifier import Classifier


class ClassifierTest(TestCase):
    def test_prediction(self):
        res = get_prediction([3.0, 2.0, 1.0], 'Usagi Studio')
        self.assertNotEqual(res, None)

    def test_huruf_converter(self):
        res = huruf_converter('A')
        self.assertEqual(res, 4.0)

    def test_hurufb_converter(self):
        res = huruf_converter('B')
        self.assertEqual(res, 3.0)

    def test_huruf_convert_lulus(self):
        res = huruf_status_converter('B')
        self.assertEqual(res, 'lulus')

    def test_huruf_convert_hati(self):
        res = huruf_status_converter('C')
        self.assertEqual(res, 'hati hati')

    def test_huruf_converter_statusd(self):
        res = huruf_status_converter('D')
        self.assertEqual(res, 'tidak lulus')

    def test_creation_passed(self):
        res = create_training_data("CSF1600400", "SDA", ["CSF1600200"])
        self.assertEqual(res[0], 'passed')

    def test_creation_none(self):
        res = create_training_data("CSF1600400", "SDA", [])
        self.assertEqual(res[0], 'passed')

    def test_creation_tidak(self):
        res = create_training_data("Usagi", "SDA", [])
        self.assertEqual(res[0], 'E')

    def test_classfier(self):
        res = Classifier('DSA')
        res.set_model("Decision Tree")

        nilai = [3, 3, 3]

        pras_mean = np.mean(nilai)
        pras_median = np.median(nilai)
        pras_std = np.std(nilai)
        pras_num = np.count_nonzero(nilai)
        input_model = np.zeros(76)

        input_model[0] = pras_mean
        input_model[1] = pras_median
        input_model[2] = pras_std
        input_model[3] = pras_num
        input_model[49] = 1

        res.predict(input_model.reshape(1, -1))
        self.assertEqual(True, True)
