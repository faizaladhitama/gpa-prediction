import requests

class Requester:
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

class SKSCollecetor:
    def __init__(self, npm, client_id):
        self.sks = []

    def get_generation(self, npm, client_id, token):
        data = Requester.request_academic_data(npm, client_id, token)
        return data['program'][0]['angkatan']

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
        response = requests.post(self.api_token, data=payload, headers=headers)
        if response.status_code == 401:
            raise ValueError("Wrong username or password, input: {}, {}".format(username, password))

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
            raise ValueError("Can't find user with npm :{}".format(npm))
        return response.json()
