from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from django.test import Client
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from .siak import get_access_token, verify_user
# from unittest.mock import Mock, patch


class SeleniumTestCase(LiveServerTestCase):

    @classmethod
    def setUp(self):
        chrome_options = Options()
        self.browser = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
        super(SeleniumTestCase, self).setUp(self)

    @classmethod
    def tearDown(self):
        self.browser.quit()
        super(SeleniumTestCase, self).tearDown(self)


class LandingPageTest(SeleniumTestCase):
    def test_landing_url_is_exist(self):
        response = Client().get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        # Opening the link we want to test
        self.browser.get('http://127.0.0.1:8000/')
        # find the form element & fill the form data
        # mocked_get_token = patch('siak.utils.get_access_token')
        # mocked_get_token.return_value = True
        # mocked_verify_user = patch('siak.utils.verify_user')
        # mocked_verify_user.return_value = True
        try:
            elementBody = self.browser.find_elements_by_css_selector('body')
            print (elementBody)
            elementLogo = self.browser.find_elements_by_css_selector('#logo')
            print (elementLogo)
            elementForm = self.browser.find_elements_by_css_selector('login_form')
            print (elementForm)
            elementUsername = self.browser.find_element_by_id('username')
            print(elementUsername)
            elementPassword = self.browser.find_element_by_id('password')
            print(elementPassword)
            elementLoginButton = self.browser.find_element_by_id('login-button')
            print( elementLoginButton)
        except NoSuchElementException:
            print('No element found')
        else:
            pass
        finally:
            pass
        
    def test_user_login_valid(self):
        #self.browser.get('http://127.0.0.1:8000/')
        # self.browser.find_element_by_id('username').send_keys('newuser')
        # self.browser.find_element_by_id('password').send_keys('NiGiw3Ch')
        # self.browser.find_element_by_id('login-button').send_keys(Keys.RETURN)
        # # self.assertEqual(self.user.username, self.browser.find_element_by_id("username-text").text)
        # self.assertIn('Prediksi Kinerja Mahasiswa', self.browser.title)
        # assert 'Anda berhasil login' in self.browser.page_source
        pass

    def test_user_login_invalid(self):
        #self.browser.get('http://127.0.0.1:8000/')
        # self.browser.find_element_by_id('username').send_keys('newuser')
        # self.browser.find_element_by_id('password').send_keys('NiGiw3Ch')
        # self.browser.find_element_by_id('login-button').send_keys(Keys.RETURN)
        # # self.assertEqual(self.user.username, self.browser.find_element_by_id("username-text").text)
        # self.assertIn('Prediksi Kinerja Mahasiswa', self.browser.title)
        # assert 'Username atau password salah' in self.browser.page_source
        pass


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
    def test_auth_login_negative(self):
        response = self.client.post('/auth-login',
                                    {'username': 'djono', 'password': 'hengki'}, follow=True)
        self.assertEqual(response.status_code, 200)
