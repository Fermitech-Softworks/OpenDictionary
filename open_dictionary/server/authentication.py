import os

from fastapi_auth0 import Auth0

auth = Auth0(domain=os.environ["DOMAIN"], api_audience=os.environ["API_AUDIENCE"],
             scopes={'openid': '', 'email': '', 'profile': ''})