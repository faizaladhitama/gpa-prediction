from unittest.mock import Mock, patch
from requests.models import Response
from django.test import TestCase
from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester
from api.db.utils import getSiakData, credentialGenerator

class UtilsTest(TestCase):
	def test_credentialGenerator(self):
		assert(credentialGenerator() == AuthGenerator.get_access_token())
	def test_getSiakData(self):
		assert(getSiakData() != null)