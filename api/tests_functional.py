from django.conf import settings
from django.test import Client
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


# class SeleniumTestCase(LiveServerTestCase):
#     @classmethod
#     def setUp(cls):
#         chrome_options = Options()
#         chrome_options.add_argument('--dns-prefetch-disable')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument("window-size=1200,640")
#         chrome_options.add_argument('disable-gpu')
#         settings.CHROME_PATH = '/usr/bin/chromedriver'
#         cls.browser = webdriver.Chrome(settings.CHROME_PATH, chrome_options=chrome_options)
#         super(SeleniumTestCase, cls).setUp(cls)

#     @classmethod
#     def tearDown(cls):
#         cls.browser.quit()
#         super(SeleniumTestCase, cls).tearDown(cls)


# class PrediktorEvaluasiAkademikTest(SeleniumTestCase):
#     """docstring for PrediktorEvaluasiAkademikTest"""

#     def test_prediktor_url_is_exist(self):
#         response = Client().get('', follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_evaluasi_tab_valid(self):
#         pass

        # self.browser.get('http://127.0.0.1:8000/')
        # self.browser.find_element_by_css_selector('#username').send_keys('admin')
        # self.browser.find_element_by_css_selector('#password').send_keys('admin')
        # self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
        # self.browser.find_element_by_css_selector('#tab-prediktor-evaluasi-akademik').click()
        # prediktor_title = \
        #     self.browser.find_element_by_css_selector('.prediktor-title').is_displayed()
        # self.assertTrue(prediktor_title)
        # prediktor_eval_button = \
        #     self.browser.find_element_by_css_selector('#prediktor-eval-button').is_displayed()
        # self.assertTrue(prediktor_eval_button)
        # prediktor_eval_msg = \
        #     self.browser.find_element_by_css_selector('.prediktor-message').is_displayed()
        # self.assertTrue(prediktor_eval_msg)

    def test_prediktor_matkul_valid(self):
        pass

         # self.browser.get('http://127.0.0.1:8000/')
         # self.browser.find_element_by_css_selector
         # ('#username').send_keys('admin')
         # self.browser.find_element_by_css_selector
         # ('#password').send_keys('admin')
         # self.browser.find_element_by_css_selector
         # ('#login-button').send_keys(Keys.RETURN)
         # self.browser.find_element_by_css_selector
         # ('#tab-prediktor-matkul').click()
         # prediktor_title = self.browser.find_element
         # _by_css_selector('.prediktor-title-matkul').is_displayed()
         # self.assertTrue(prediktor_title)
         # matkul_to_predict = self.browser.find_element_by_css_
         # selector('.matkul-to-predict').is_displayed()
         # self.assertTrue(matkul_to_predict)
         # prediktor_matkul_button = self.browser.find_element_by
         # _css_selector('#result-button').is_displayed()
         # self.assertTrue(prediktor_matkul_button)
         # table_matkul_prasyarat = self.browser.find_element_by
         # _css_selector('#table-matkul-prasyarat').is_displayed()
         # self.assertTrue(table_matkul_prasyarat)
         # prediktor_eval_msg = self.browser.find_element_by_css_selector
         # ('.prediktor-message').is_displayed()
         # self.assertTrue(prediktor_eval_msg)


    def test_predik_eval_invalid(self):
        pass


# class LandingPageTest(SeleniumTestCase):
#     def test_landing_url_is_exist(self):
#         response = Client().get('', follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_user_login(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         element_body = self.browser.find_elements_by_css_selector('body')
#         print("body ", element_body)
#         element_logo = self.browser.find_elements_by_css_selector('#logo')
#         print("logo ", element_logo)
#         element_form = self.browser.find_elements_by_css_selector('.login_form')
#         print("form ", element_form)
#         element_username = self.browser.find_elements_by_css_selector('#username')
#         print("username ", element_username)
#         element_password = self.browser.find_elements_by_css_selector('#password')
#         print("password ", element_password)
#         element_login_button = self.browser.find_elements_by_css_selector('#login-button')
#         print("login button ", element_login_button)

#     def test_user_login_mahasiswa_valid(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         self.browser.find_element_by_css_selector('#username').send_keys('admin')
#         self.browser.find_element_by_css_selector('#password').send_keys('admin')
#         self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
#         wait(self.browser, 15).until(EC.url_changes('mahasiswa/'))
#         self.assertIn("Anda berhasil login", self.browser.page_source)

#     def test_user_login_invalid(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         self.browser.find_element_by_css_selector('#username').send_keys('mola')
#         self.browser.find_element_by_css_selector('#password').send_keys('molo')
#         self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
#         self.assertIn("Username atau password salah", self.browser.page_source)

#     def test_user_logout(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         self.browser.find_element_by_css_selector('#username').send_keys('admin')
#         self.browser.find_element_by_css_selector('#password').send_keys('admin')
#         self.browser.find_element_by_css_selector('#login-button').send_keys(Keys.RETURN)
#         print(self.browser.find_element_by_css_selector('#navbar-dropdown'))
#         self.browser.find_element_by_css_selector('#navbar-dropdown').click()
#         self.browser.find_element_by_css_selector('#logout-button').click()
#         self.assertIn("Anda berhasil logout.",
#                       self.browser.page_source)
