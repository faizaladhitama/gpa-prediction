from api.siak.utils import AuthGenerator, Requester
import os

def get_academic_record(npm):
	sso_uname = 'gibran.muhammad' #os.environ['SSO_USERNAME']
	sso_pwd = 'cyprogram241' #os.environ['SSO_PASSWORD']

	ag = AuthGenerator()

	client_id = ag.get_client_id()
	token = ag.get_access_token(sso_uname, sso_pwd)

	print(ag.verify_user(token)['username'])
	if(ag.verify_user(token)['username'] == sso_uname):
		res = Requester.request_academic_data(npm, client_id, token)
		return res
	else:
		raise Exception("Failed to verificate token")
