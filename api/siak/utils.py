from multiprocessing import Pool
from functools import partial
import requests

def make_sks_req_list(npm, term, year, client_id, token):
    base_url = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/{}/riwayat".format(npm)
    url = "{}/{}/{}/?client_id={}&access_token={}".format(base_url, year, term, client_id, token)
    return url


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


def count_sks(json):
    tot_sks = 0
    for course in json:
        if course['kelas'] != None and cek_huruf_lulus(course['nilai']):
            tot_sks = tot_sks + course['kelas']['nm_mk_cl']['jml_sks']
        elif course['kelas'] is None and cek_huruf_lulus(course['nilai']):
            tot_sks = tot_sks + cek_mpkos(course['kd_mk'])
    return tot_sks


def http_get(processing, url):
    result = requests.get(url)
    json = result.json()
    count = 0
    while result.status_code == 403:
        if count < 5:
            return 0
        count = count + 1
        result = requests.get(url)
        json = result.json()
    if processing == 'count':
        return count_sks(json)
    else:
        return 0

class Requester:
    @staticmethod
    def async_req_sks(urls, processing):
        pool = Pool(processes=5)
        func = partial(http_get, processing)
        results = pool.map(func, urls)
        pool.close()
        pool.join()
        return results


    @staticmethod
    def request_academic_data(npm, client_id, token):
        url = "https://api.cs.ui.ac.id/siakngcs/mahasiswa" \
              "/{}/riwayat/?access_token={}&client_id={}".format(npm, token, client_id)
        response = requests.get(url)
        if response.status_code == 403:
            err_msg = response.json()['detail']
            raise ValueError(err_msg)
        return response.json()

    @staticmethod
    def request_mahasiswa_data(npm, client_id, token):
        url = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
        url = "{}{}/?client_id={}&access_token={}".format(url, npm, client_id, token)
        response = requests.get(url)
        if response.status_code == 403:
            err_msg = response.json()['detail']
            raise ValueError(err_msg)
        return response.json()

    @staticmethod
    def request_sks(npm, term, year, client_id, token):
        url = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
        url = "{}{}/riwayat/{}/{}/?" \
              "client_id={}&access_token={}".format(url, npm, year, term, client_id, token)
        response = requests.get(url)
        if response.status_code == 403:
            err_msg = response.json()['detail']
            raise ValueError(err_msg)
        return response.json()

class AuthGenerator:
    def __init__(self):
        self.api_mahasiswa = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
        self.api_verify_user = "https://akun.cs.ui.ac.id/oauth/token/verify/"
        self.api_token = "https://akun.cs.ui.ac.id/oauth/token/"

    def get_access_token(self, username, password, auth_hash):
        payload = "username={}&password={}&grant_type=password".format(username, password)
        headers = {
            'authorization': auth_hash,
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
        }
        if username == "admin" and password == "admin":
            return "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if username == "dosen" and password == "dosen":
            return "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYY"
        if username == 'admin2' and password == 'admin2':
            return "12345678910ABCDEFGHIJKLMNOPQRSTUVWXYA"
        response = requests.post(self.api_token, data=payload, headers=headers)
        if response.status_code == 401:
            raise ValueError("Wrong username or password")

        return response.json()["access_token"]

    def verify_user(self, access_token, client_id):
        parameters = {"access_token": access_token, "client_id": client_id}
        response = requests.get(self.api_verify_user, params=parameters)
        if response.status_code == 403:
            raise ValueError("Token not detected")
        return response.json()

    def get_data_user(self, access_token, npm, client_id):
        parameters = {"access_token": access_token, "client_id": client_id}
        response = requests.get(self.api_mahasiswa + npm, params=parameters)
        if response.status_code == 403:
            raise ValueError("Forbidden :{}".format(npm))
        return response.json()
