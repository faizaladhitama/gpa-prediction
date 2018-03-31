from django.test import TestCase
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87

>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87

class PrediktorKelulusanMatkulTest(TestCase):
    def test_prediktor_matkul_url_exist(self):
        response = self.client.post('/mahasiswa/prediktor-matkul', follow=True)
        self.assertEqual(response.status_code, 200)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    def test_rekomendasi(self):
        response = self.client.get('/mahasiswa/rekomendasi', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/mahasiswa/profile', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_prediktor_evaluasi(self):
        response = self.client.get('/mahasiswa/prediktor_evaluasi', follow=True)
        self.assertEqual(response.status_code, 404)
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
