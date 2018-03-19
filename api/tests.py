from django.test import TestCase
from sso.csui_helper import get_access_token, verify_user, get_data_user, get_client_id

class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)