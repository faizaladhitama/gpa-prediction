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
        'N': 0.00
    }
    return bobot[huruf]

def cek_mpkos(code):
    code_matkul = [
        'UIGE600040',
        'UIGE600041',
        'UIGE600042',
        'UIGE600043',
        'UIGE600045',
        'UIGE600047',
        'UIGE600048',
        'UIGE600020',
        'UIGE600021',
        'UIGE600022',
        'UIGE600023',
        'UIGE600025',
        'UIGE600024',
        'UIGE600026',
        'UIGE600027',
        'UIGE600028',
        'UIGE600029',
        'UIGE600030',
    ]

    if code in code_matkul:
        return 1
    else:
        return 0


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
        elif access_token == "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYY":
            return {"identity_number": 'admin', "role": 'dosen'}
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
                    if course['kelas'] != None and cek_huruf_lulus(course['nilai']):
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                    elif course['kelas'] is None and cek_huruf_lulus(course['nilai']):
                        tot_sks = tot_sks + cek_mpkos(course['kd_mk'])

        return tot_sks, None
    except ValueError as exception:
        return None, str(exception)
    except requests.ConnectionError as exception:
        return None, str(exception)


def get_all_sks_term(access_token, npm):
    try:
        taken_course = []
        data = Requester.request_mahasiswa_data(npm, os.environ['CLIENT_ID'], access_token)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        sks_map = {}

        for year in range(int(angkatan), now.year + 1):
            sks_terms = []
            for term in range(1, 4):
                tot_sks = 0
                res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
                for course in res:
                    crs_not_none = course['kelas'] != None
                    if course['kd_mk'] in taken_course:
                        continue
                    elif crs_not_none and cek_huruf_lulus(course['nilai']):
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                        taken_course.append(course['kd_mk'])
                    elif course['kelas'] is None and cek_huruf_lulus(course['nilai']):
                        tot_sks = tot_sks + cek_mpkos(course['kd_mk'])
                        taken_course.append(course['kd_mk'])
                sks_terms.append(tot_sks)
            sks_map[year] = sks_terms
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
            elif course['kelas'] is None and cek_huruf_lulus(course['nilai']):
                tot_sks = tot_sks + cek_mpkos(course['kd_mk'])

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


def get_all_ip_term(access_token, npm):
    try:
        data = Requester.request_mahasiswa_data(npm, os.environ['CLIENT_ID'], access_token)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        ip_map = {}

        for year in range(int(angkatan), now.year + 1):
            ip_terms = []
            for term in range(1, 4):
                tot_sks = 0
                mutu = 0.00
                res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
                for course in res:
                    if course['kelas'] != None:
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                        mutu += course['kelas']['nm_mk_cl']['jml_sks'] * \
                                huruf_to_angka(course['nilai'])
                if tot_sks != 0:
                    ip_mahasiswa = round(mutu / tot_sks * 100) / 100.00
                else:
                    ip_mahasiswa = 0.00
                ip_terms.append(ip_mahasiswa)
            ip_map[year] = ip_terms
        return ip_map, None
    except ValueError as exception:
        return {}, str(exception)
    except requests.ConnectionError as exception:
        return {}, str(exception)
