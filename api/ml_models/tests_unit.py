from django.test import TestCase

from api.ml_models import get_prediction, \
    huruf_converter, huruf_status_converter, create_training_data
from api.ml_models.classifier import Classifier


class NbModelTest(TestCase):
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
        res = Classifier('DSA', columns=['hasil', 'pras2'], num_features=['pras2'])
        res.build_model()
        self.assertEqual(True, True)
