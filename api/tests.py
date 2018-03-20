from django.test import TestCase

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
