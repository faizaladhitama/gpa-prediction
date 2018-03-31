import requests

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
        response = requests.post(self.api_token, data=payload, headers=headers)

        if response.status_code == 401:
            raise Exception("Wrong username or password, input: {}, {}".format(username, password,))
