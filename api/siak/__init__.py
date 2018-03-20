from api.siak.utils import AuthGenerator, Requester

def get_academic_record(npm, username, password):
    generator = AuthGenerator()

    client_id = generator.get_client_id()
    token = generator.get_access_token(username, password)

    if generator.verify_user(token)['username'] == username:
        res = Requester.request_academic_data(npm, client_id, token)
        return res
    else:
        return False

def get_access_token(username, password):
    generator = AuthGenerator()
    return generator.get_access_token(username, password)

def verify_user(access_token):
    generator = AuthGenerator()
    return generator.verify_user(access_token)

def get_data_user(access_token, npm):
    generator = AuthGenerator()
    return generator.get_data_user(access_token, npm)
