from django.test import TestCase
from sso.csui_helper import get_access_token, verify_user, get_data_user, get_client_id

class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)

class APICredentialGenerator(TestCase):
    def test_get_clientid:
        assert(get_client_id() == "X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG")
    def test_get_access_token:
        pass
    

