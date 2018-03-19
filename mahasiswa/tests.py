from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/mahasiswa', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_rekomendasi(self):
        response = self.client.get('/mahasiswa/rekomendasi', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/mahasiswa/profile', follow=True)
        self.assertEqual(response.status_code, 200)


class ElementTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homepage(self):
        resp = self.client.get('/mahasiswa')
        self.assertNotContains(response=resp, text="<h10>", status_code=301)

    def test_page_title(self):
        driver = self.driver()
        driver.get('http://localhost:8000')
        self.assertIn('Homepage', driver.title)
        self.fail('Finish the test!')

    def test_klik_tab_prediksi_kelulusan_matkul(self):
        pass    

    def test_search_bar_blank_search(self):
        element = driver.find_element_by_id('search-bar')
        element.send_keys('', Keys.RETURN)
        assert "No results found." not in driver.page_source
    
    def tearDown(self):
        self.driver.close()      
