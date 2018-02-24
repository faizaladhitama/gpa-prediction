from django.test import TestCase
from django.urls import reverse
from django.template import RequestContext
from django.template.loader import render_to_string

class DummyTests(TestCase):

    def test_dummy(self):
        self.assertIs(True, True)

    def test_html(self):
        response = self.client.get('')
        self.assertIs(response.status_code, 200)
