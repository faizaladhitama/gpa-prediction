class SSOClient:
    """
    This class is responsible for communicating with SSOAuth client
    Any SSO related service should be implemented here.
    """

    def __init__(self, data):
        pass

    def generate_token(self):
        """ Generate message to be send to SSOAuth client """
        pass

    def login(self, user):
        """ Login to SSOAuth client using generated token """
        pass

    def logout(self, user):
        """ Logout  """
        pass

    def create_session(self, sname, payload=None):
        """ Create user session  """
        pass

    def delete_session(self, sname):
        """ Delete user session """
        pass
