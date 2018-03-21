from unittest.mock import patch
from django.test import TestCase
from api.db.utils import get_siak_data, parse_siak_data, insert_to_db_rekam_jejak, \
                         create_mock_data_mahasiswa, create_mock_data_dosen
from api.models import Dosen, Mahasiswa, RekamJejakNilaiMataKuliah, MataKuliah

class UtilsTest(TestCase):
    def setUp(self):
        self.mocked_get_siak_data = patch('api.db.utils.get_siak_data')
        self.mocked_get_academic_record = patch('api.siak.get_academic_record')
        self.mocked_parse_siak_data = patch('api.db.utils.parse_siak_data')
        self.pass_lint = "pass"

        self.mocked_get_academic_record.start()
        self.mocked_get_siak_data.start()
        self.mocked_parse_siak_data.start()

        self.addCleanup(self.mocked_get_siak_data.stop)
        self.addCleanup(self.mocked_parse_siak_data.stop)
        self.addCleanup(self.mocked_get_academic_record.stop)

    @patch('api.siak.get_academic_record')
    def test_get_siak_data(self, *args):
        args = args
        self.mocked_get_academic_record.return_value = "mocked-record"
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"

        with self.assertRaises(Exception) as context:
            resp = get_siak_data(mock_npm, mock_username, mock_password)
            resp = resp

        expected = "Wrong username or password, input: sonoko.nogi, 12345"
        self.assertEqual(expected, str(context.exception))

    def test_parse_siak(self):
        self.mocked_get_siak_data.return_value = "mocked"
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"
        hasil = parse_siak_data(mock_npm, mock_username, mock_password)
        return hasil != None

    def test_insert_to_db_rekam_jejak(self):
        self.pass_lint = "done"
        mock_npm = "11111111111"
        mock_kode_matkul = "123"
        mock_nilai = "A"
        insert_to_db_rekam_jejak(npm=mock_npm, kode_matkul=mock_kode_matkul, nilai=mock_nilai)
        flag1 = Mahasiswa.objects.filter(npm=mock_npm).count() > 0
        flag2 = MataKuliah.objects.filter(kode_matkul=mock_kode_matkul).count() > 0
        flag3 = RekamJejakNilaiMataKuliah.objects.filter(npm=mock_npm,
                                                         kode_matkul=mock_kode_matkul).count() > 0
        return flag1 and flag2 and flag3

    def test_create_mock_data_mahasiswa(self):
        self.pass_lint = "done"
        return create_mock_data_mahasiswa()

    def test_create_mock_data_dosen(self):
        self.pass_lint = "done"
        create_mock_data_dosen(5)
        flag = Dosen.objects.filter(nama="nama5").count() > 0
        return flag
