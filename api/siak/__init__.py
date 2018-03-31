from api.siak.utils import AuthGenerator

def get_academic_record(npm, username, password):
    print(npm)
    generator = AuthGenerator()
    generator.get_client_id()
    generator.get_access_token(username, password)
