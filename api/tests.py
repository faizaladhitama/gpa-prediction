from django.test import TestCase


class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('login', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
        response = self.client.get('logout', follow=True)
        self.assertEqual(response.status_code, 404)
