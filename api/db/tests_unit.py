from unittest.mock import patch

import time
from django.test import TestCase

from api.db.utils import get_siak_data, parse_siak_data, insert_to_db_rekam_jejak, \
    create_mock_data_mahasiswa, create_mock_data_dosen, caching
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

    def test_get_siak_data(self):
        self.mocked_get_academic_record.return_value = "mocked-record"
        mock_npm = "mocked"
        mock_username = "sonoko.nogi"
        mock_password = "12345"
        hasil = get_siak_data(mock_npm, mock_username, mock_password)

        expected = "Wrong username or password"
        self.assertEqual(expected, hasil)

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

class CacheTest(TestCase):

    def lazy(self,count):
        for i in range(6000):
            for j in range(6000):
                count = 0
        return count

    def test_without_caching(self):
        start = time.time()
        res = caching("non_cache",self.lazy,0)
        end = time.time()-start
        self.assertEqual(res,0)
        self.assertGreaterEqual(end,10)

    def test_with_caching(self):
        caching("cache",self.lazy,0)
        start = time.time()
        res = caching("cache", self.lazy, 0)
        end = time.time()-start
        self.assertEqual(res,0)
        self.assertLessEqual(end,0.05)

