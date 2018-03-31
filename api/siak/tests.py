from unittest.mock import Mock, patch

import requests
from django.test import TestCase

from api.siak import get_academic_record, get_access_token, verify_user, get_data_user
from api.siak.utils import AuthGenerator, Requester


def create_mocked_response(status_code, data):
    mocked_response = Mock(spec=requests.Response)
    mocked_response.status_code = status_code
    mocked_response.json.return_value = data
    return mocked_response


class RequesterTest(TestCase):
    def setUp(self):
        mocked_get = patch('requests.get')

        self.mocked_get = mocked_get.start()
        self.addCleanup(mocked_get.stop)

    def test_request_data_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        resp = Requester.request_academic_data(mock_npm, mock_access_token, mock_client_id)
        self.assertEqual("mocked", resp["mocked"])

    def test_request_data_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_npm = "mocked"
        mock_access_token = "mocked"
        mock_client_id = "mocked"

        with self.assertRaises(Exception) as context:
            Requester.request_academic_data(mock_npm, mock_access_token, mock_client_id)

        self.assertTrue("mocked" in str(context.exception))


class UtilsTest(TestCase):
    def setUp(self):
        mocked_post = patch('requests.post')
        mocked_get = patch('requests.get')

        self.generator = AuthGenerator()
        self.mocked_post = mocked_post.start()
        self.mocked_get = mocked_get.start()
        self.addCleanup(mocked_post.stop)
        self.addCleanup(mocked_get.stop)

    def test_get_client_id(self):
        client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
        self.assertEqual(client_id, self.generator.get_client_id())

    def test_get_token_on_valid(self):
        self.mocked_post.return_value = create_mocked_response(200, {"access_token": 1})

        mock_uname = "mocked"
        mock_pswd = "mocked"

        resp = self.generator.get_access_token(mock_uname, mock_pswd)
        self.assertEqual(1, resp)

    def test_get_token_on_invalid(self):
        self.mocked_post.return_value = create_mocked_response(401, {})

        mock_uname = "mocked"
        mock_pswd = "mocked"

        with self.assertRaises(Exception) as context:
            self.generator.get_access_token(mock_uname, mock_pswd)

        self.assertTrue('mocked' in str(context.exception))

    def test_verify_user_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_access_token = "mocked"

        resp = self.generator.verify_user(mock_access_token)
        self.assertEqual("mocked", resp["mocked"])

    def test_verify_user_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_access_token = "mocked"

        with self.assertRaises(Exception) as context:
            self.generator.verify_user(mock_access_token)

        self.assertTrue("mocked" in str(context.exception))

    def test_get_data_user_on_valid(self):
        self.mocked_get.return_value = create_mocked_response(200, {"mocked": "mocked"})

        mock_access_token = "mocked"
        mock_npm = "mocked"

        resp = self.generator.get_data_user(mock_access_token, mock_npm)
        self.assertEqual("mocked", resp["mocked"])

    def test_get_data_user_on_invalid(self):
        self.mocked_get.return_value = create_mocked_response(403, {"detail": "mocked"})

        mock_access_token = "mocked"
        mock_npm = "mocked"

        with self.assertRaises(Exception) as context:
            self.generator.get_data_user(mock_access_token, mock_npm)

        self.assertTrue('mocked' in str(context.exception))


class SiakTest(TestCase):
    def setUp(self):
        mocked_generator = patch('api.siak.utils.AuthGenerator.__init__')
        mocked_get_token = patch('api.siak.utils.AuthGenerator.get_access_token')
        mocked_get_id = patch('api.siak.utils.AuthGenerator.get_client_id')
        mocked_verify = patch('api.siak.utils.AuthGenerator.verify_user')
        mocked_get_data = patch('api.siak.utils.AuthGenerator.get_data_user')
        mocked_requester = patch('api.siak.utils.Requester.request_academic_data')

        self.mocked_generator = mocked_generator.start()
        self.mocked_verify = mocked_verify.start()
        self.mocked_get_id = mocked_get_id.start()
        self.mocked_get_token = mocked_get_token.start()
        self.mocked_get_data = mocked_get_data.start()
        self.mocked_requester = mocked_requester.start()

        self.addCleanup(mocked_generator.stop)
        self.addCleanup(mocked_requester.stop)
        self.addCleanup(mocked_verify.stop)
        self.addCleanup(mocked_get_token.stop)
        self.addCleanup(mocked_get_data.stop)
        self.addCleanup(mocked_get_id.stop)

        self.mock_npm = "mocked"
        self.mock_username = "kafuu.chino"
        self.mock_password = "1"

    def test_get_record_on_valid(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = {"username": "kafuu.chino"}
        self.mocked_requester.return_value = "mocked"
        self.mocked_get_id.return_value = 1
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("mocked", resp)

    def test_get_record_on_invalid(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = {"username": "mocked"}
        self.mocked_requester.return_value = "mocked"
        self.mocked_get_id.return_value = 1
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("Failed to verificate token", resp)

    def test_get_record_on_value_error(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.side_effect = ValueError("mocked error")
        self.mocked_get_id.return_value = 1
        self.mocked_get_token.return_value = 1

        resp = get_academic_record(self.mock_npm, self.mock_username, self.mock_password)

        self.assertEqual("mocked error", resp)

    def test_get_record_on_conn_error(self):
        self.mocked_generator.return_value = None
        self.mocked_get_token.side_effect = requests.ConnectionError("connection refused")

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

    def test_get_data_on_valid(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.return_value = {"mocked": "mocked"}

        resp = get_data_user(mocked_token, self.mock_npm)

        self.assertEqual("mocked", resp["mocked"])

    def test_get_data_on_value_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.side_effect = ValueError("mocked error")

        resp = get_data_user(mocked_token, self.mock_npm)

        self.assertEqual("mocked error", resp)

    def test_get_data_on_conn_error(self):
        mocked_token = "mocked"

        self.mocked_generator.return_value = None
        self.mocked_get_data.side_effect = requests.ConnectionError("connection refused")

        resp = get_data_user(mocked_token, self.mock_npm)

        self.assertEqual("connection refused", resp)
