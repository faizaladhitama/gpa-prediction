from unittest.mock import Mock, patch

import datetime
import requests
from django.test import TestCase

from django.core.cache import cache
from api.siak import get_academic_record, get_access_token, \
    verify_user, get_data_user, get_jenjang, get_all_sks_term, \
    get_sks_term, get_ip_term, get_all_ip_term, get_sks_sequential, \
    get_total_mutu, get_mata_kuliah

from api.siak.utils import AuthGenerator, Requester, \
    make_sks_req_list


def create_mocked_response(status_code, data):
    mocked_response = Mock(spec=requests.Response)
    mocked_response.status_code = status_code
    mocked_response.json.return_value = data
    return mocked_response


class UtilsTest(TestCase):
    def setUp(self):
        mocked_get = patch('requests.get')

        self.mocked_get = mocked_get.start()
        self.addCleanup(mocked_get.stop)

    # def test_httpget_on_valid(self):
    #     course = {'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'kd_mk':'UIGE600042', 'nilai': 'B-'}
    #     data = [course]
    #     self.mocked_get.return_value = create_mocked_response(200, data)

    #     count = http_get('count', 'mocked')
    #     self.assertEqual(3, count)

    #     course = {'kelas': None, 'kd_mk':'UIGE600042', 'nilai': 'B-'}
    #     data = [course]
    #     self.mocked_get.return_value = create_mocked_response(200, data)

    #     count = http_get('count', 'mocked')
    #     self.assertEqual(1, count)

    #     count = http_get('other', 'mocked')
    #     self.assertEqual(0, count)

    def test_url_formatter(self):
        url = make_sks_req_list("0", 0, 0, "0", "0")
        self.assertEqual(url, "https://api-dev.cs.ui.ac.id/"+\
            "siakngcs/mahasiswa/0/riwayat/0/0/?client_id=0&access_token=0")


class RequesterTest(TestCase):
    def setUp(self):
        mocked_get = patch('requests.get')

        self.mocked_get = mocked_get.start()
        self.addCleanup(mocked_get.stop)

    def test_request_sks_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_npm = "mocked"
        mock_token = "mocked"
        mock_client_id = "mocked"
        mock_term = 1
        mock_year = 1512

        resp = Requester.request_sks(mock_npm, mock_term, mock_year, mock_client_id, mock_token)
        self.assertEqual("mocked", resp["mocked"])

    def test_request_sks_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_npm = "mocked"
        mock_token = "mocked"
        mock_client_id = "mocked"
        mock_term = 1
        mock_year = 1512

        with self.assertRaises(ValueError) as context:
            Requester.request_sks(mock_npm, mock_term, mock_year, mock_client_id, mock_token)

        self.assertTrue("mocked" in str(context.exception))

    def test_request_md_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        resp = Requester.request_mahasiswa_data(mock_npm, mock_client_id, mock_access_token)
        self.assertEqual("mocked", resp["mocked"])

    def test_request_md_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        with self.assertRaises(ValueError) as context:
            Requester.request_mahasiswa_data(mock_npm, mock_client_id, mock_access_token)

        self.assertTrue("mocked" in str(context.exception))

    def test_request_data_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        resp = Requester.request_academic_data(mock_npm, mock_client_id, mock_access_token)
        self.assertEqual("mocked", resp["mocked"])

    def test_request_data_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        with self.assertRaises(ValueError) as context:
            Requester.request_academic_data(mock_npm, mock_client_id, mock_access_token)

        self.assertTrue("mocked" in str(context.exception))


class AuthGeneratorTest(TestCase):
    def setUp(self):
        mocked_post = patch('requests.post')
        mocked_get = patch('requests.get')

        self.generator = AuthGenerator()
        self.mocked_post = mocked_post.start()
        self.mocked_get = mocked_get.start()
        self.addCleanup(mocked_post.stop)
        self.addCleanup(mocked_get.stop)

    def test_get_token_on_valid(self):
        self.mocked_post.return_value = create_mocked_response(200, {"access_token": 1})

        mock_uname = "mocked"
        mock_pswd = "mocked"
        mock_hash = "mocked"

        resp = self.generator.get_access_token(mock_uname, mock_pswd, mock_hash)
        self.assertEqual(1, resp)

    def test_get_token_on_invalid(self):
        self.mocked_post.return_value = create_mocked_response(401, {})

        mock_uname = "mocked"
        mock_pswd = "mocked"
        mock_hash = "mocked"

        with self.assertRaises(Exception) as context:
            self.generator.get_access_token(mock_uname, mock_pswd, mock_hash)

        self.assertTrue('Wrong username or password' in str(context.exception))

    def test_verify_user_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_access_token = "mocked"
        mock_client_id = "mocked"

        resp = self.generator.verify_user(mock_access_token, mock_client_id)
        self.assertEqual("mocked", resp["mocked"])

    def test_verify_user_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_access_token = "mocked"
        mock_client_id = "mocked"

        with self.assertRaises(ValueError) as context:
            self.generator.verify_user(mock_access_token, mock_client_id)

        self.assertEqual("Token not detected", str(context.exception))

    def test_get_data_user_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_access_token = "mocked"
        mock_npm = "mocked"
        mock_client_id = "mocked"

        resp = self.generator.get_data_user(mock_access_token, mock_npm, mock_client_id)
        self.assertEqual("mocked", resp["mocked"])

    def test_get_data_user_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_access_token = "mocked"
        mock_npm = "mocked"
        mock_client_id = "mocked"

        with self.assertRaises(Exception) as context:
            self.generator.get_data_user(mock_access_token, mock_npm, mock_client_id)

        self.assertTrue('mocked' in str(context.exception))


class MockSiak(TestCase):
    def setUp(self):
        mocked_generator = patch('api.siak.utils.AuthGenerator.__init__')
        #mocked_asyc_req = patch('api.siak.utils.Requester.async_req_sks')
        mocked_get_token = patch('api.siak.utils.AuthGenerator.get_access_token')
        mocked_verify = patch('api.siak.utils.AuthGenerator.verify_user')
        mocked_get_data = patch('api.siak.utils.AuthGenerator.get_data_user')
        mocked_requester = patch('api.siak.utils.Requester.request_academic_data')
        mocked_req_sks = patch('api.siak.utils.Requester.request_sks')
        mocked_req_sks_seq = patch('api.siak.get_sks_sequential')
        mocked_req_data = patch('api.siak.utils.Requester.request_mahasiswa_data')
        mocked_dict_for_sks_term = patch('mahasiswa.utils.convert_dict_for_sks_term')
        mocked_get_jenjang = patch('api.siak.get_jenjang')
        mocked_get_sks_sequential = patch('api.siak.get_sks_sequential')
        mocked_create_graph_ip = patch('mahasiswa.utils.create_graph_ip')
        mocked_convert_dict_for_ip_term = patch('mahasiswa.utils.convert_dict_for_ip_term')
        mocked_get_all_sks_term = patch('api.siak.get_all_sks_term')
        mocked_get_matkul = patch('api.siak.get_mata_kuliah')

        self.mocked_generator = mocked_generator.start()
        #self.mocked_asyc_req = mocked_asyc_req.start()
        self.mocked_verify = mocked_verify.start()
        self.mocked_get_token = mocked_get_token.start()
        self.mocked_get_data = mocked_get_data.start()
        self.mocked_requester = mocked_requester.start()
        self.mocked_req_sks = mocked_req_sks.start()
        self.mocked_req_sks_seq = mocked_req_sks_seq.start()
        self.mocked_req_data = mocked_req_data.start()
        self.mocked_dict_for_sks_term = mocked_dict_for_sks_term.start()
        self.mocked_get_jenjang = mocked_get_jenjang.start()
        self.mocked_get_sks_sequential = mocked_get_sks_sequential.start()
        self.mocked_create_graph_ip = mocked_create_graph_ip.start()
        self.mocked_convert_dict_for_ip_term = mocked_convert_dict_for_ip_term.start()
        self.mocked_get_all_sks_term = mocked_get_all_sks_term.start()
        self.mocked_get_matkul = mocked_get_matkul.start()

        #self.addCleanup(mocked_asyc_req.stop)
        self.addCleanup(mocked_generator.stop)
        self.addCleanup(mocked_requester.stop)
        self.addCleanup(mocked_verify.stop)
        self.addCleanup(mocked_get_token.stop)
        self.addCleanup(mocked_get_data.stop)
        self.addCleanup(mocked_req_sks.stop)
        self.addCleanup(mocked_req_sks_seq.stop)
        self.addCleanup(mocked_req_data.stop)
        self.addCleanup(mocked_dict_for_sks_term.stop)
        self.addCleanup(mocked_get_sks_sequential.stop)
        self.addCleanup(mocked_get_jenjang.stop)
        self.addCleanup(mocked_create_graph_ip.stop)
        self.addCleanup(mocked_convert_dict_for_ip_term.stop)
        self.addCleanup(mocked_get_all_sks_term.stop)
        self.addCleanup(mocked_get_matkul.stop)

        self.mock_npm = "mocked"
        self.mock_username = "kafuu.chino"
        self.mock_password = "1"
        self.mock_token = 'mocked'


class SiakTest(MockSiak):
    def test_get_record_on_valid(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = {"username": "kafuu.chino"}
        self.mocked_requester.return_value = "mocked"
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("mocked", resp)

    def test_get_record_on_invalid(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = {"username": "mocked"}
        self.mocked_requester.return_value = "mocked"
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("Failed to verificate token", resp)

    def test_get_record_on_value_error(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.side_effect = ValueError("mocked error")
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("mocked error", resp)

    def test_get_record_on_conn_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = requests.ConnectionError("connection refused")

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("connection refused", resp)

    def test_get_record_on_http_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = requests.HTTPError("connection refused")

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("connection refused", resp)

    def test_get_token_on_valid(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.return_value = 1

        resp = get_access_token(self.mock_username, self.mock_password)
        self.assertEqual(1, resp)

    def test_get_token_on_value_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = ValueError("mocked error")

        resp = get_access_token(self.mock_username, self.mock_password)
        self.assertEqual("mocked error", resp)

    def test_get_token_on_conn_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = requests.ConnectionError("connection refused")

        resp = get_access_token(self.mock_username, self.mock_password)

        self.assertEqual("connection refused", resp)

    def test_get_token_on_http_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = requests.HTTPError("connection refused")

        resp = get_access_token(self.mock_username, self.mock_password)

        self.assertEqual("connection refused", resp)

    def test_verify_user_on_valid(self):
        mocked_data = {"username": "kafuu.chino"}
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = mocked_data

        resp = verify_user(mocked_token)

        self.assertEqual(mocked_data, resp)

    def test_verify_user_on_value_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_verify.side_effect = ValueError("mocked error")

        resp = verify_user(mocked_token)

        self.assertEqual("mocked error", resp)

    def test_verify_user_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_verify.side_effect = requests.ConnectionError("connection refused")

        resp = verify_user(mocked_token)

        self.assertEqual("connection refused", resp)

    def test_verify_user_on_http_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_verify.side_effect = requests.HTTPError("connection refused")

        resp = verify_user(mocked_token)

        self.assertEqual("connection refused", resp)

    def test_get_data_on_valid(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.return_value = {"mocked": "mocked"}

        resp, err = get_data_user(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual("mocked", resp["mocked"])

    def test_get_data_on_value_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.side_effect = ValueError("mocked error")

        resp, err = get_data_user(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("mocked error", err)

    def test_get_data_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_data_user(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("connection refused", err)

    def test_get_data_on_http_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.side_effect = requests.HTTPError("connection refused")

        resp, err = get_data_user(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("connection refused", err)

    def test_get_sks_seq_on_valid(self):
        mocked_token = "mocked"

        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        course1 = {'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'A'}
        course2 = {'kelas': None, 'kd_mk':'UIGE600040', 'nilai': 'A'}
        course3 = {'kelas': None, 'kd_mk':'UIGE600001', 'nilai': 'A'}
        mocked_sks = [course1, course2, course3]
        self.mocked_req_sks.return_value = mocked_sks

        now = datetime.datetime.now()

        resp, err = get_sks_sequential(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual(4 * (now.year + 1 - 2015) * 3, resp)


    def test_get_sks_seq_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_sks_sequential(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("connection refused", err)

    def test_get_sks_seq_on_http_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = requests.HTTPError("connection refused")

        resp, err = get_sks_sequential(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("connection refused", err)

    def test_get_sks_seq_on_val_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = ValueError("mocked error")

        resp, err = get_sks_sequential(mocked_token, self.mock_npm)

        self.assertIsNone(resp)
        self.assertEqual("mocked error", err)

    @patch('api.siak.get_data_user')
    def test_get_jenjang_on_valid(self, mocked_get_data):
        mocked_token = "mocked"
        mocked_get_data.return_value = ({"program": [{"nm_prg": "S1 Regular"}]}, None)

        program, err = get_jenjang(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual("S1 Regular", program)

    @patch('api.siak.get_data_user')
    def test_get_jenjang_on_invalid(self, mocked_get_data):
        mocked_token = "mocked"
        mocked_get_data.return_value = (None, "mocked error")

        program, err = get_jenjang(mocked_token, self.mock_npm)

        self.assertIsNone(program)
        self.assertEqual("mocked error", err)

    def test_get_all_sks_term_on_valid(self):
        mocked_token = "mocked"

        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        course1 = {'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'kd_mk':'UIGE600042', 'nilai': 'B-'}
        course2 = {'kelas': None, 'kd_mk':'UIGE600040', 'nilai': 'A'}
        course3 = {'kelas': None, 'kd_mk':'UIGE600001', 'nilai': 'A'}
        mocked_sks = [course1, course2, course3]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_all_sks_term(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual({2015: [4, 0, 0], 2016: [0, 0, 0], 2017: [0, 0, 0], 2018: [0, 0, 0]}, resp)

    def test_get_all_sks_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_all_sks_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_get_all_sks_on_http_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = requests.HTTPError("connection refused")

        resp, err = get_all_sks_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_get_all_sks_on_val_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = ValueError("mocked error")

        resp, err = get_all_sks_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("mocked error", err)

    def test_get_sks_term_on_valid(self):
        mocked_token = "mocked"
        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'B-'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertIsNone(err)
        self.assertEqual(3, resp)
        cache.clear()

        mocked_sks = [{'kelas': None, 'nilai': 'B-', 'kd_mk':'UIGE600001'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertIsNone(err)
        self.assertEqual(0, resp)
        cache.clear()

        mocked_sks = [{'kelas': None, 'nilai': 'B-', 'kd_mk':'UIGE600040'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertIsNone(err)
        self.assertEqual(1, resp)
        cache.clear()

        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'C-'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertIsNone(err)
        self.assertEqual(0, resp)
        cache.clear()

        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'N'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertIsNone(err)
        self.assertEqual(0, resp)
        cache.clear()

    def test_get_sks_term_on_conn_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_get_sks_term_on_http_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = requests.HTTPError("connection refused")

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_get_sks_term_on_val_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = ValueError("connection refused")

        resp, err = get_sks_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_get_ip_term_on_valid(self):
        mocked_token = "mocked"
        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'B-'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_ip_term(mocked_token, self.mock_npm, 2015, 2)

        self.assertIsNone(err)
        self.assertEqual(2.7, resp)

    def test_get_ip_term_on_conn_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_ip_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_get_ip_term_on_http_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = requests.HTTPError("connection refused")

        resp, err = get_ip_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_get_ip_term_on_val_error(self):
        mocked_token = "mocked"
        self.mocked_req_sks.side_effect = ValueError("connection refused")

        resp, err = get_ip_term(mocked_token, self.mock_npm, 1997, 3)

        self.assertEqual(0, resp)
        self.assertEqual("connection refused", err)

    def test_all_ip_term_valid_0(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 0}}, 'nilai': 'N'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_all_ip_term(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual({2015: [0, 0, 0], 2016: [0, 0, 0],
                          2017: [0, 0, 0], 2018: [0, 0, 0]}, resp)

    def test_all_ip_term_on_valid(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'B-'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_all_ip_term(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual({2015: [2.7, 2.7, 2.7], 2016: [2.7, 2.7, 2.7],
                          2017: [2.7, 2.7, 2.7], 2018: [2.7, 2.7, 2.7]}, resp)

    def test_all_ip_term_on_conn_error(self):
        mocked_token = "mocked"
        self.mocked_req_data.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_all_ip_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_all_ip_term_on_http_error(self):
        mocked_token = "mocked"
        self.mocked_req_data.side_effect = requests.HTTPError("connection refused")

        resp, err = get_all_ip_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)


    def test_all_ip_term_on_val_error(self):
        mocked_token = "mocked"

        self.mocked_req_data.side_effect = ValueError("connection refused")

        resp, err = get_all_ip_term(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_get_total_mutu_on_valid(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        mocked_sks = [{'kelas': {'nm_mk_cl': {'jml_sks': 3}}, 'nilai': 'A'}]
        self.mocked_req_sks.return_value = mocked_sks

        resp, err = get_total_mutu(mocked_token, self.mock_npm)

        self.assertIsNone(err)
        self.assertEqual(144.0, resp)

    def test_total_mutu_on_conn_error(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        self.mocked_req_sks.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_total_mutu(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_total_mutu_on_http_error(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        self.mocked_req_sks.side_effect = requests.HTTPError("connection refused")

        resp, err = get_total_mutu(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_total_mutu_on_val_error(self):
        mocked_token = "mocked"
        self.mocked_req_data.return_value = {'program': [{'angkatan': 2015}]}

        self.mocked_req_sks.side_effect = ValueError("connection refused")

        resp, err = get_total_mutu(mocked_token, self.mock_npm)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_get_matkul_on_valid(self):
        mocked_token = "mocked"

        self.mocked_get_matkul.return_value = {
            "url": "https://api.cs.ui.ac.id/siakngcs/matakuliah/1490/", \
            "kd_mk": "UIGE600021", "nm_mk": "MPK Seni - Batik", \
            "kd_org": "02.00.12.01", "kd_kur": "02.00.12.01-2016", "jml_sks": 1}
        resp, err = get_mata_kuliah(mocked_token)

        mocked_res = {"url": "https://api.cs.ui.ac.id/siakngcs/matakuliah/1490/", \
            "kd_mk": "UIGE600021", "nm_mk": "MPK Seni - Batik", \
            "kd_org": "02.00.12.01", "kd_kur": "02.00.12.01-2016", "jml_sks": 1}
        self.assertIsNone(err)
        self.assertEqual(mocked_res, resp)

    def test_get_matkul_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_get_matkul.side_effect = requests.ConnectionError("connection refused")

        resp, err = get_mata_kuliah(mocked_token)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)

    def test_get_matkul_on_val_error(self):
        mocked_token = "mocked"
        self.mocked_get_matkul.side_effect = ValueError("connection refused")

        resp, err = get_mata_kuliah(mocked_token)

        self.assertEqual({}, resp)
        self.assertEqual("connection refused", err)
