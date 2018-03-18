import os
from api.siak.utils import AuthGenerator, Requester

def get_academic_record(npm):
    sso_uname = os.environ['SSO_USERNAME']
    sso_pwd = os.environ['SSO_PASSWORD']

    generator = AuthGenerator()

    client_id = generator.get_client_id()
    token = generator.get_access_token(sso_uname, sso_pwd)

    print(generator.verify_user(token)['username'])
    if generator.verify_user(token)['username'] == sso_uname:
        res = Requester.request_academic_data(npm, client_id, token)
        return res
    else:
        raise Exception("Failed to verificate token")
