from unittest.mock import Mock, patch
from requests.models import Response
from django.test import TestCase
from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester
from api.db.utils import *

class UtilsTest(TestCase):
    
    def setUp(self):
        mocked_get_siak_data = patch('api.db.getSiakData') 
        mocked_parse_siak_data = patch('api.db.parseSiakData')

        self.mocked_get_siak_data.start()
        self.mocked_parse_siak_data.start()

        self.addCleanup(mocked_get_siak_data.stop)
        self.addCleanup(mocked_parse_siak_data.stop)

    def test_getSiakData(self):
        self.mocked_generator.return_value = None
        self.mocked_verify.return_value = {"username":"sonoko.nogi"}
        self.mocked_requester.return_value = "mocked"
        self.mocked_get_id.return_value = 1
        self.mocked_get_token.return_value = 1
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"

        resp = getSiakData(mock_npm, mock_username, mock_password)

        self.assertEqual("mocked", resp)
    
    def test_ParseSiak(self):
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"
        hasil = parseSiakDataToDb(mock_npm, mock_username, mock_password)
        self.assertEqual("ABC",hasil)

    def test_insertToDbRekamJejakAllNull(self):
        mock_npm = "11111111111"
        mock_kode_matkul = "123"
        mock_nilai = "A"
        #kesavedong :()
        return True

    def test_createMockDataDosen(self):
        return True