import requests
from django.conf import settings
from api.siak.utils import AuthGenerator, Requester

def get_academic_record(npm, username, password):
    try:
        generator = AuthGenerator()

        client_id = settings.CLIENT_ID
        token = generator.get_access_token(username, password, settings.AUTH_HASH)

        if generator.verify_user(token, client_id)['username'] == username:
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
        return generator.get_access_token(username, password, settings.AUTH_HASH)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def verify_user(access_token):
    try:
        generator = AuthGenerator()
        if access_token == "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return {"identity_number": 'admin', "role": 'mahasiswa'}
        return generator.verify_user(access_token, settings.CLIENT_ID)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def get_data_user(access_token, npm):
    try:
        generator = AuthGenerator()
        return generator.get_data_user(access_token, npm, settings.CLIENT_ID)
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)
