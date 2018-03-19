from api.siak import get_academic_record, get_access_token
from api.siak.utils import AuthGenerator, Requester

def credentialGenerator(self):
	token = get_access_token(self, muhammad.faiz52, 15kukusan)
	return token

def getSiakData(self, npm, username, password):
	#kalo buat semuanya paling ITF , yang kita cuma bisa ambil 6 aja
	res = get_academic_record(npm, username, password)
	print(res)
	return res
	
def insertToDb(self):
	pass

def populateDbWithMock(self):
	pass

def createMockData(self):
	pass