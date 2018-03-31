from datetime import datetime

from django.test import TestCase

from mahasiswa.utils import getTerm, getContextMahasiswa


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


class UnitTest(TestCase):
    def test_term_1(self):
        now = datetime(2018, 4, 1)
        self.assertEqual(getTerm(now), "2017/2018 - 2")

    def test_term_2(self):
        now = datetime(2018, 9, 1)
        self.assertEqual(getTerm(now), "2018/2019 - 1")

    def test_term_3(self):
        now = datetime(2018, 7, 1)
        self.assertEqual(getTerm(now), "2017/2018 - 3")

    def test_context_mahasiswa_valid(self):
        session = {
            'user_login': 'dummy',
            'kode_identitas': 'dummy',
            'role': 'dummy'
        }
        request = MockRequest(session)
        getContextMahasiswa(request, getTerm(datetime.now()))

    def test_context_mahasiswa_invalid_request(self):
        request = None
        getContextMahasiswa(request, getTerm(datetime.now()))

    def test_context_mahasiswa_invalid_session(self):
        request = MockRequest()
        getContextMahasiswa(request, getTerm(datetime.now()))
