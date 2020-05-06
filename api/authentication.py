from functools import wraps
from models.users import Users
from flask import request


def check_token_wrapper(func):
    """check token validity"""
    @wraps(func)
    def auth():
        token = None
        try:
            auth_header = request.headers.get('Authorization')
            print(auth_header)
            token = auth_header.split(" ")[0]
            if Users.decode_token(token):
                return func(token)
        except Exception as ex:
            return ex
    return auth
