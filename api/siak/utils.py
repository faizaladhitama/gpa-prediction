import requests

class Requester:
    @staticmethod
    def request_academic_data(npm, client_id, token):
        url = "https://api.cs.ui.ac.id/siakngcs/mahasiswa" \
              "/{}/riwayat/?access_token={}&client_id={}".format(npm, token, client_id)
        response = requests.get(url)
        if response.status_code == 403:
            err_msg = response.json()['detail']
            raise ValueError("Can't find user with npm :{}".format(npm))
        return response.json()

    @staticmethod
    def request_mahasiswa_data(npm, client_id, token):

    @staticmethod
    def request_sks(npm, term, year, client_id, token):

class AuthGenerator:
    def __init__(self):
        self.api_mahasiswa = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
        self.api_verify_user = "https://akun.cs.ui.ac.id/oauth/token/verify/"
        self.api_token = "https://akun.cs.ui.ac.id/oauth/token/"
        self.client_id = "X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"

    def get_client_id(self):
        return self.client_id

    def get_access_token(self, username, password):
        payload = "username={}&password={}&grant_type=password".format(username, password)
        auth_hash = "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RD" \
                    "l6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5T" \
                    "UxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0" \
                    "doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA=="
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

    def verify_user(self, access_token):
        parameters = {"access_token": access_token, "client_id": self.get_client_id()}
        response = requests.get(self.api_verify_user, params=parameters)
        if response.status_code == 403:
            raise ValueError("Token not detected")
        return response.json()

    def get_data_user(self, access_token, npm):
        parameters = {"access_token": access_token, "client_id": self.get_client_id()}
        response = requests.get(self.api_mahasiswa + npm, params=parameters)
        if response.status_code == 403:
            raise ValueError("Can't find user with npm :{}".format(npm))
        return response.json()
