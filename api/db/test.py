from unittest.mock import Mock, patch
from requests.models import Response
from django.test import TestCase
from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester
from api.db.utils import *

class UtilsTest(TestCase):
    
    def setUp(self):
        self.mocked_get_siak_data = patch('api.db.utils.getSiakData')
        self.mocked_get_academic_record = patch('api.siak.get_academic_record') 
        self.mocked_parse_siak_data = patch('api.db.utils.parseSiakData')

        self.mocked_get_academic_record.start()
        self.mocked_get_siak_data.start()
        self.mocked_parse_siak_data.start()

        self.addCleanup(self.mocked_get_siak_data.stop)
        self.addCleanup(self.mocked_parse_siak_data.stop)
        self.addCleanup(self.mocked_get_academic_record.stop)

    @patch('api.siak.get_academic_record')    
    def test_getSiakData(self, *args):
        self.mocked_get_academic_record.return_value = "mocked-record"
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"

        with self.assertRaises(Exception) as context:
            resp = getSiakData(mock_npm, mock_username, mock_password)

        expected = "Wrong username or password, input: sonoko.nogi, 12345"
        self.assertEqual(expected, str(context.exception))
    
    def test_ParseSiak(self):
        self.mocked_get_siak_data.return_value = "mocked"
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"
        hasil = parseSiakData(mock_npm, mock_username, mock_password)
        return hasil != None 

    def test_insertToDbRekamJejakAllNull(self):
        mock_npm = "11111111111"
        mock_kode_matkul = "123"
        mock_nilai = "A"
        insertToDbRekamJejak(npm=mock_npm, kode_matkul=mock_kode_matkul, nilai=mock_nilai)
        flag1 = Mahasiswa.objects.filter(npm=mock_npm).count() > 0
        flag2 =  MataKuliah.objects.filter(kode_matkul=mock_kode_matkul).count() > 0
        flag3 =  RekamJejakNilaiMataKuliah.objects.filter(npm=mock_npm, 
                                                          kode_matkul=mock_kode_matkul).count() > 0
        return flag1 and flag2 and flag3

    def test_createMockDataMahasiswa(self):
        return createMockDataMahasiswa()

    def test_createMockDataDosen(self):
        createMockDataDosen(5)
        flag = Dosen.objects.filter(nama="nama5").count() > 0
        return flag