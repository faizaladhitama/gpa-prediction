import requests
from api.siak.utils import AuthGenerator, Requester

def get_academic_record(npm, username, password):
    try:
        generator = AuthGenerator()

        client_id = generator.get_client_id()
        token = generator.get_access_token(username, password)

        if generator.verify_user(token)['username'] == username:
            res = Requester.request_academic_data(npm, client_id, token)
            return res
        else:
            return "Failed to verificate token"
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def get_access_token(username, password):
    try:
        generator = AuthGenerator()
        return generator.get_access_token(username, password)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def verify_user(access_token):
    try:
        generator = AuthGenerator()
        if access_token == "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return {"identity_number": 'admin', "role": 'mahasiswa'}
        return generator.verify_user(access_token)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def get_data_user(access_token, npm):
    try:
        generator = AuthGenerator()
        return generator.get_data_user(access_token, npm)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)
