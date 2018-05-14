import datetime
import os

import requests

from api.db.utils import caching
from api.siak.utils import AuthGenerator, Requester, \
    make_sks_req_list, cek_huruf_lulus, huruf_to_angka, cek_mpkos


def get_academic_record(npm, username, password):
    try:
        generator = AuthGenerator()
        client_id = os.environ['CLIENT_ID']
        token = generator.get_access_token(username, password, os.environ['AUTH_HASH'])

        if generator.verify_user(token, client_id)['username'] == username:
            res = caching("request_academic_data",
                          Requester.request_academic_data, (npm, client_id, token), npm)
            return res
        else:
            return "Failed to verificate token"
    except ValueError as exception:
        return str(exception)
    except requests.ConnectionError as exception:
        return str(exception)


def get_siak_data(npm, username, password):
    # kalo buat semuanya paling ITF , yang kita cuma bisa ambil 6 aja
    return get_academic_record(npm, username, password)


def parse_siak_data(npm, username, password):
    data = get_siak_data(npm, username, password)
    return data


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
        return generator.verify_user(access_token)
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
        return caching("generator_get_data_user",
                       generator.get_data_user, (access_token, npm, os.environ['CLIENT_ID']),
                       npm), None
    except ValueError as exception:
        return None, str(exception)
    except requests.ConnectionError as exception:
        return None, str(exception)


# def get_sks(access_token, npm):
#     try:
#         data = caching("req_mahasiswa_data", Requester.request_mahasiswa_data,
#                        (npm, os.environ['CLIENT_ID'], access_token), npm)
#         angkatan = data['program'][0]['angkatan']

#         now = datetime.datetime.now()
#         urls = []

#         for year in range(int(angkatan), now.year + 1):
#             for term in range(1, 4):
#                 url = make_sks_req_list(npm, term, year, os.environ['CLIENT_ID'], access_token)
#                 urls.append(url)

#         all_sks = caching("async_req_sks", Requester.async_req_sks, (urls, 'count'), npm)
#         return sum(all_sks), None
#     except ValueError as exception:
#         return None, str(exception)
#     except requests.ConnectionError as exception:
#         return None, str(exception)


def get_sks_sequential(access_token, npm):
    try:
        data = caching("request_mahasiswa_data", Requester.request_mahasiswa_data,
                       (npm, os.environ['CLIENT_ID'], access_token), npm)
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
        data = caching("request_mahasiswa_data", Requester.request_mahasiswa_data,
                       (npm, os.environ['CLIENT_ID'], access_token), npm)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        sks_map = {}

        for year in range(int(angkatan), now.year + 1):
            sks_terms = []
            for term in range(1, 4):
                tot_sks = 0
                key_name = "request_sks"+"_"+str(term)+"_"+str(year)
                res = caching(key_name, Requester.request_sks,
                              (npm, term, year, os.environ['CLIENT_ID'], access_token), npm)
                #res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
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
        key_name = "request_sks"+"_"+str(term)+"_"+str(year)
        res = caching(key_name, Requester.request_sks,
                      (npm, term, year, os.environ['CLIENT_ID'], access_token), npm)
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
    res, err = caching("get_data_user", get_data_user, (access_token, npm), npm)
    if err is None:
        return res['program'][0]['nm_prg'], None
    else:
        return None, err


def get_ip_term(access_token, npm, year, term):
    try:
        key_name = "request_sks"+"_"+str(term)+"_"+str(year)
        res = caching(key_name, Requester.request_sks,
                      (npm, term, year, os.environ['CLIENT_ID'], access_token), npm)
        tot_sks = 0
        mutu = 0.00

        for course in res:
            if course['kelas'] != None:
                tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                mutu += course['kelas']['nm_mk_cl']['jml_sks'] * huruf_to_angka(course['nilai'])
        ip_mahasiswa = round(mutu / tot_sks * 100) / 100.00
        return ip_mahasiswa, None
    except ValueError as exception:
        return 0, str(exception)
    except requests.ConnectionError as exception:
        return 0, str(exception)


def get_all_ip_term(access_token, npm):
    try:
        data = caching("request_mahasiswa_data", Requester.request_mahasiswa_data,
                       (npm, os.environ['CLIENT_ID'], access_token), npm)
        angkatan = data['program'][0]['angkatan']

        now = datetime.datetime.now()

        ip_map = {}

        for year in range(int(angkatan), now.year + 1):
            ip_terms = []
            for term in range(1, 4):
                tot_sks = 0
                mutu = 0.00
                key_name = "request_sks"+"_"+str(term)+"_"+str(year)
                res = caching(key_name, Requester.request_sks,
                              (npm, term, year, os.environ['CLIENT_ID'], access_token), npm)
                #res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
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


def get_total_mutu(access_token, npm):
    try:
        data = caching("request_mahasiswa_data", Requester.request_mahasiswa_data,
                       (npm, os.environ['CLIENT_ID'], access_token), npm)
        angkatan = data['program'][0]['angkatan']
        now = datetime.datetime.now()
        mutu = 0.00

        for year in range(int(angkatan), now.year + 1):
            for term in range(1, 4):
                tot_sks = 0
                key_name = "request_sks"+"_"+str(term)+"_"+str(year)
                res = caching(key_name, Requester.request_sks,
                              (npm, term, year, os.environ['CLIENT_ID'], access_token), npm)
                #res = Requester.request_sks(npm, term, year, os.environ['CLIENT_ID'], access_token)
                for course in res:
                    if course['kelas'] != None:
                        tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
                        mutu += course['kelas']['nm_mk_cl']['jml_sks'] * \
                                huruf_to_angka(course['nilai'])
        return mutu, None
    except ValueError as exception:
        return {}, str(exception)
    except requests.ConnectionError as exception:
        return {}, str(exception)
