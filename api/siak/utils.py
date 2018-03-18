import requests

class AuthGenerator:
    def __init__(self):
        self.API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
        self.API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"
        self.API_TOKEN = "https://akun.cs.ui.ac.id/oauth/token/"
    
    def get_client_id(self):
        client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
        return client_id

    def get_access_token(self, username, password):
        payload = "username={}&password={}&grant_type=password".format(username, password)
        headers = {
        'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
        }
        response = requests.post(self.API_TOKEN, data=payload, headers=headers)

        if(response.status_code == 401):
        	raise Exception("Wrong username or password, input : [{}, {}]".format(username, password,))

        return response.json()["access_token"]
            
    def verify_user(self, access_token):
        parameters = {"access_token": access_token, "client_id": self.get_client_id()}
        response = requests.get(self.API_VERIFY_USER, params=parameters)
        if(response.status_code == 403):
        	raise Exception("{} input : {}".format(response.json()['detail'], access_token))
        return response.json()

    def get_data_user(self, access_token, npm):
        parameters = {"access_token": access_token, "client_id": self.get_client_id()}
        response = requests.get(self.API_MAHASISWA+npm, params=parameters)
        if(response.status_code == 403):
        	raise Exception("{} input : [{}, {}]".format(response.json()['detail'],access_token, npm))
        return response.json()

class Requester:

    @staticmethod
    def request_academic_data(npm, client_id, token):
        url = 'https://api.cs.ui.ac.id/siakngcs/mahasiswa/{}/riwayat/?access_token={}&client_id={}'.format(npm, token, client_id)
        response = requests.get(url)
        if(response.status_code == 403):
        	raise Exception("{} input : [{}, {}, {}]".format(response.json()['detail'], npm, client_id, token))
        return response.json()