from datetime import datetime

from django.test import TestCase

from mahasiswa.utils import get_term, get_context_mahasiswa, \
    get_evaluation_detail_message, get_semester, \
    get_angkatan


class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/mahasiswa/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_rekomendasi(self):
        response = self.client.get('/mahasiswa/rekomendasi', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/mahasiswa/profile', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_prediktor_evaluasi(self):
        response = self.client.get('/mahasiswa/prediktor_evaluasi', follow=True)
        self.assertEqual(response.status_code, 404)


class MockRequest:
    def __init__(self, session=None):
        if session is None:
            session = {}
        self.session = session


class TermTest(TestCase):
    def test_term_1(self):
        now = datetime(2018, 4, 1)
        self.assertEqual(get_term(now), "2017/2018 - 2")

    def test_term_2(self):
        now = datetime(2018, 9, 1)
        self.assertEqual(get_term(now), "2018/2019 - 1")

    def test_term_3(self):
        now = datetime(2018, 7, 1)
        self.assertEqual(get_term(now), "2017/2018 - 3")


class ContextTest(TestCase):
    def test_context_mahasiswa_valid(self):
        session = {
            'user_login': 'dummy',
            'kode_identitas': 'dummy',
            'role': 'dummy'
        }
        request = MockRequest(session)
        context = get_context_mahasiswa(request, get_term(datetime.now()))
        self.assertEqual(context, {'term': '2017/2018 - 2', 'team': 'usagi studio',
                                   'user': 'dummy', 'id': 'dummy', 'role': 'dummy'})

    def test_context_invalid_request(self):
        request = None
        context = get_context_mahasiswa(request, get_term(datetime.now()))
        self.assertEqual(context, "'NoneType' object has no attribute 'session'")

    def test_context_invalid_session(self):
        request = MockRequest()
        context = get_context_mahasiswa(request, get_term(datetime.now()))
        self.assertEqual(context, "'user_login'")


class EvaluationTest(TestCase):
    def test_detail_valid_all(self):
        detail_message = get_evaluation_detail_message("S1", 2)
        source = detail_message['source']
        detail = detail_message['detail']
        self.assertEqual(None, source)
        self.assertEqual(None, detail)

    def test_detail_valid_semester_only(self):
        detail_message = get_evaluation_detail_message("S1", -1)
        source = detail_message['source']
        detail = detail_message['detail']
        self.assertEqual(None, source)
        self.assertEqual(None, detail)

    def test_detail_valid_ip_only(self):
        detail_message = get_evaluation_detail_message("S-teh", 2)
        source = detail_message['source']
        detail = detail_message['detail']
        self.assertEqual(None, source)
        self.assertEqual(None, detail)

    def test_detail_invalid_all(self):
        detail_message = get_evaluation_detail_message("S-teh", -1)
        source = detail_message['source']
        detail = detail_message['detail']
        self.assertEqual(None, source)
        self.assertEqual(None, detail)


class SemesterTest(TestCase):
    def test_semester_2_term(self):
        semester = get_semester("15066989162", 2)
        self.assertEqual(6, semester)

    def test_semester_1_term(self):
        semester = get_semester("15066989162", 1)
        self.assertEqual(6, semester)

    def test_semester_3_term(self):
        semester = get_semester("15066989162", 3)
        self.assertEqual(6, semester)

    def test_term_invalid(self):
        semester = get_semester("15066989162", 4)
        self.assertEqual("Wrong term", semester)

    def kode_identitas_invalid(self):
        semester = get_semester("-15066989162", 4)
        self.assertEqual("Wrong kode identitas", semester)


class AngkatanTest(TestCase):
    def test_angkatan_valid(self):
        angkatan = get_angkatan("15066989162")
        self.assertEqual(2015, angkatan)

    def test_angkatan_invalid(self):
        angkatan = get_angkatan("-1506689162")
        self.assertEqual("Wrong kode identitas", angkatan)
