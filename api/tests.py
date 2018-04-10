from django.conf import settings
from django.test import Client
from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class SeleniumTestCase(LiveServerTestCase):
    @classmethod
    def setUp(cls):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("window-size=1200,640")
        chrome_options.add_argument('disable-gpu')
        print(settings.CHROME_PATH)
        cls.browser = webdriver.Chrome(settings.CHROME_PATH, chrome_options=chrome_options)
        super(SeleniumTestCase, cls).setUp(cls)

    @classmethod
    def tearDown(cls):
        cls.browser.quit()
        super(SeleniumTestCase, cls).tearDown(cls)


class LandingPageTest(SeleniumTestCase):
    def test_landing_url_is_exist(self):
        response = Client().get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        self.browser.get('http://127.0.0.1:8000/')
        element_body = self.browser.find_elements_by_css_selector('body')
        print("body ", element_body)
        element_logo = self.browser.find_elements_by_css_selector('#logo')
        print("logo ", element_logo)
        element_form = self.browser.find_elements_by_css_selector('.login_form')
        print("form ", element_form)
        element_username = self.browser.find_elements_by_css_selector('#username')
        print("username ", element_username)
        element_password = self.browser.find_elements_by_css_selector('#password')
        print("password ", element_password)
        element_login_button = self.browser.find_elements_by_css_selector('#login-button')
        print("login button ", element_login_button)

    def test_user_login_mahasiswa_valid(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_css_selector('#username').send_keys('admin')
        self.browser.find_element_by_css_selector('#password').send_keys('admin')
        self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
        wait(self.browser, 15).until(EC.url_changes('mahasiswa/'))
        self.assertIn("Anda berhasil login", self.browser.page_source)

    def test_user_login_invalid(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_css_selector('#username').send_keys('mola')
        self.browser.find_element_by_css_selector('#password').send_keys('molo')
        self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
        self.assertIn("Username atau password salah", self.browser.page_source)

    def test_user_logout(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_css_selector('#username').send_keys('admin')
        self.browser.find_element_by_css_selector('#password').send_keys('admin')
        self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
        print(self.browser.find_element_by_css_selector('#navbar-dropdown'))
        self.browser.find_element_by_css_selector('#navbar-dropdown').click()
        self.browser.find_element_by_css_selector('#logout-button').click()
        self.assertIn("Anda berhasil logout. Semua session Anda sudah dihapus",
                      self.browser.page_source)


class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_login(self):
        response = self.client.get('/auth-login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/index', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_landing(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)


class UserTest(TestCase):
    def test_auth_login_positive(self):
        response = self.client.post('/auth-login',
                                    {'username': 'admin', 'password': 'admin'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_login_negative(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola'}, follow=True)
        self.assertEqual(response.status_code, 200)


class ExternalAPITest(TestCase):
    def test_ui_server_up(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ui_server_down(self):
        response = self.client.post('/auth-login',
                                    {'username': 'molo', 'password': 'mola', 'connection': False},
                                    follow=True)
        self.assertEqual(response.status_code, 200)

class ViewProfileMahasiswa(SeleniumTestCase):
    def test_profile_mahasiswa_is_exist(self):
        pass

    def test_view_profile_mahasiswa(self):
        pass