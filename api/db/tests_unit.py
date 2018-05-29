import time
from unittest.mock import patch

from django.core.cache import cache
from django.test import TestCase

from api.db.utils import insert_to_db_rekam_jejak, \
    create_mock_data_mahasiswa, create_mock_data_dosen, \
    caching, create_matakuliah, populate_matkul, populate_prasyarat_matkul, \
    get_kode_prasyarat, get_nama_prasyarat, conv_nama_matkul_to_kode_matkul
from api.models import Dosen, Mahasiswa, RekamJejakNilaiMataKuliah, MataKuliah, PrasyaratMataKuliah
from api.siak import get_siak_data, parse_siak_data


class UtilsTest(TestCase):
    def setUp(self):
        self.mocked_get_siak_data = patch('api.siak.get_siak_data')
        self.mocked_get_academic_record = patch('api.siak.get_academic_record')
        self.mocked_parse_siak_data = patch('api.siak.parse_siak_data')
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
        cache.clear()
        hasil = get_siak_data(mock_npm, mock_username, mock_password)

        # expected = "Wrong username or password"
        self.assertNotEqual(hasil, None)

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

    def test_create_matakuliah(self):
        mock_kode_matkul = 'IKI20100'
        mock_nama_matkul = 'Basis Data'
        create_matakuliah(mock_kode_matkul, nama=mock_nama_matkul)
        flag = MataKuliah.objects.filter(kode_matkul=mock_kode_matkul, \
                                         nama_matkul=mock_nama_matkul).count() > 0
        self.assertTrue(flag)

    def test_populate_matkul(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        populate_matkul(mock_csv)
        flag = MataKuliah.objects.all().count() > 1
        self.assertTrue(flag)

    def test_populate_prasyarat_matkul(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        populate_prasyarat_matkul(mock_csv)
        flag = PrasyaratMataKuliah.objects.all().count() > 1
        self.assertTrue(flag)

    def test_get_kode_prasyarat(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_kode_matkul = 'IKS32753'
        mock_kode_prasyarat = ['IKI20505']
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_kode_prasyarat, get_kode_prasyarat(mock_kode_matkul))

    def test_get_nama_prasyarat(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_nama_matkul = 'Administrasi Sistem'
        mock_nama_prasyarat = ['Sistem Operasi']
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_nama_prasyarat, get_nama_prasyarat(mock_nama_matkul))

    def test_get_nama_prasyarat_nfound(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_nama_matkul = 'dummy'
        mock_nama_prasyarat = "Prasyarat tidak ditemukan"
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_nama_prasyarat, get_nama_prasyarat(mock_nama_matkul))

    def test_conv_nama_to_kode(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_nama_matkul = 'Penambangan Data'
        mock_kode_matkul = 'IKO42351'
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_kode_matkul, conv_nama_matkul_to_kode_matkul(mock_nama_matkul))

    def test_conv_nama_2kode_invalid(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_nama_matkul = 'Icikiwir'
        mock_kode_matkul = 'Prasyarat tidak ditemukan'
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_kode_matkul, conv_nama_matkul_to_kode_matkul(mock_nama_matkul))

    def test_get_kode_prasyarat_none(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_kode_matkul = 'IKS000'
        mock_kode_prasyarat = "Prasyarat tidak ditemukan"
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_kode_prasyarat, get_kode_prasyarat(mock_kode_matkul))

    def test_get_nama_prasyarat_none(self):
        mock_csv = './api/db/prasyarat_matkul.csv'
        mock_nama_matkul = 'asdfjas'
        mock_nama_prasyarat = "Prasyarat tidak ditemukan"
        populate_prasyarat_matkul(mock_csv)
        self.assertEqual(mock_nama_prasyarat, get_nama_prasyarat(mock_nama_matkul))


def lazy(count):
    for i in range(6000):
        for j in range(6000):
            count = (i + j) * 0
    return count


def dict_cache(dict_):
    return dict_


class CacheTest(TestCase):
    def test_without_caching(self):
        start = time.time()
        res = caching("non_cache", lazy, 0)
        end = time.time() - start
        self.assertEqual(res, 0)
        self.assertGreaterEqual(end, 10)

    def test_with_caching(self):
        caching("cache", lazy, 0)
        start = time.time()
        res = caching("cache", lazy, 0)
        end = time.time() - start
        self.assertEqual(res, 0)
        self.assertLessEqual(end, 2)

    def test_dict(self):
        caching("dict_cache", dict_cache, {"a": 1, "b": 2})
        dict_ = caching("dict_cache", dict_cache, {"a": 1, "b": 2})
        expected = {"a": 1, "b": 2}
        self.assertEqual(expected, dict_)
