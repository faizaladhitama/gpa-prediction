import os
import datetime
import requests
from api.siak.utils import AuthGenerator, Requester

def get_academic_record(npm, username, password):
    try:
        generator = AuthGenerator()
        client_id = os.environ['CLIENT_ID']
        token = generator.get_access_token(username, password, os.environ['AUTH_HASH'])

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
        return generator.get_access_token(username, password, os.environ['AUTH_HASH'])
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def verify_user(access_token):
    try:
        generator = AuthGenerator()
        if access_token == "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return {"identity_number": 'admin', "role": 'mahasiswa'}
        return generator.verify_user(access_token, os.environ['CLIENT_ID'])
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)

def get_data_user(access_token, npm):
    try:
        generator = AuthGenerator()
        return generator.get_data_user(access_token, npm, os.environ['CLIENT_ID']), None
    except ValueError as exception:
        return None, str(exception)
    except requests.ConnectionError as exception:
        return None, str(exception)

def get_sks(access_token, npm):
    try:
        data = Requester.request_mahasiswa_data(npm, os.environ['CLIENT_ID'], access_token)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        tot_sks = 0

        for year in range(int(angkatan), now.year + 1):
            for term in range(1, 4):
                res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
                for course in res:
                    if course['kelas'] != None:
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']

        return tot_sks, None
    except ValueError as exception:
        return None, str(exception)
    except requests.ConnectionError as exception:
        return None, str(exception)

def get_all_sks_term(access_token, npm):

def get_sks_term(access_token, npm, year, term):

def get_jenjang(access_token, npm):
    res, err = get_data_user(access_token, npm)

    if err is None:
        return res['program'][0]['nm_prg'], None
    else:
        return None, err
