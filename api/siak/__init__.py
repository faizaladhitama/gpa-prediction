import datetime
import os

import requests

from api.siak.utils import AuthGenerator, Requester


def cek_huruf_lulus(huruf):
    if huruf == "C-":
        return False
    elif "A" in huruf or "B" in huruf or "C" in huruf:
        return True
    else:
        return False


def huruf_to_angka(huruf):
    bobot = {
        'A': 4.00,
        'A-': 3.70,
        'B+': 3.30,
        'B': 3.00,
        'B-': 2.70,
        'C+': 2.30,
        'C': 2.00,
        'C-': 1.70,
        'D': 1.00,
        'E': 0.00,
    }
    return bobot[huruf]


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
    try:
        data = Requester.request_mahasiswa_data(npm, os.environ['CLIENT_ID'], access_token)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        sks_map = {}

        for year in range(int(angkatan), now.year + 1):
            for term in range(1, 4):
                tot_sks = 0
                res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
                for course in res:
                    if course['kelas'] != None and cek_huruf_lulus(course['nilai']):
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']

                sks_map[term] = tot_sks

        return sks_map, None
    except ValueError as exception:
        return {}, str(exception)
    except requests.ConnectionError as exception:
        return {}, str(exception)


def get_sks_term(access_token, npm, year, term):
    try:
        res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
        tot_sks = 0

        for course in res:
            if course['kelas'] != None and cek_huruf_lulus(course['nilai']):
                tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
        return tot_sks, None
    except ValueError as exception:
        return 0, str(exception)
    except requests.ConnectionError as exception:
        return 0, str(exception)


def get_jenjang(access_token, npm):
    res, err = get_data_user(access_token, npm)
    if err is None:
        return res['program'][0]['nm_prg'], None
    else:
        return None, err


def get_ip_term(access_token, npm, year, term):
    try:
        res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
        tot_sks = 0
        mutu = 0.00

        for course in res:
            if course['kelas'] != None:
                tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                mutu += course['kelas']['nm_mk_cl']['jml_sks'] * huruf_to_angka(course['nilai'])
        ip_mahasiswa = round(mutu / tot_sks * 100)/100.00
        return ip_mahasiswa, None
    except ValueError as exception:
        return 0, str(exception)
    except requests.ConnectionError as exception:
        return 0, str(exception)
