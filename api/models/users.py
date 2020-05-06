from database import database
import psycopg2
from datetime import datetime, timedelta
import time
import jwt
import os


class Users(database.DatabaseManager):
    def __init__(self, user_data, isAdmin=False, user_id=None):
        super().__init__()
        self.user_id = user_id
        self.name = user_data[0]
        self.username = user_data[1]
        self.email = user_data[3]
        self.password = user_data[2]
        self.isAdmin = isAdmin

    def create_new_user(self):
        sql = "INSERT INTO \"NovelNarrative\".users(name, username, email, password)" \
              " VALUES ('{}', '{}', '{}', '{}')".format(self.name, self.username, self.email, self.password)
        self.insert_into_database(sql)

    def query_login(self):
        sql = "SELECT * FROM \"NovelNarrative\".users WHERE \"NovelNarrative\".users.username = '{}'".format(self.username)
        user_info = self.get_user(sql)
        self.user_id = user_info['user_id'].values[0]
        self.name = user_info['name'].values[0]
        self.email = user_info['email'].values[0]
        return Users(user_data=[self.name, self.username, self.password, self.email], user_id=self.user_id)

    def generate_auth_token(self, expiration=60000):
        try:
            secret_key = os.environ.get("NOVELNARRATIVESECRETKEY", b'G\x0e\x07\x94\xf3ASGP\xe9\x98\x82\x07[\\\xeeq\xda =\xbf3$*')
            dt = (datetime.now() + timedelta(minutes=expiration))
            time_dt = time.mktime(dt.timetuple())
            datet = datetime.now()
            time_date = time.mktime(datet.timetuple())
            payload = {
                'exp': time_dt,
                'iat': time_date,
                'sub': int(self.user_id)
            }
            print(payload)
            print(secret_key)

            return payload
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def decode_token(token):
        try:
            return token
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError()
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError()

    @staticmethod
    def check_not_is_timed_out(token):
        """Check that the token is not in the auth_token table"""
        try:
            connection = database.DatabaseManager()
            isTimedout = database.DatabaseManager.get_token(connection,
                                                            "SELECT * FROM auth_token WHERE token = {}".format(token))
            if isTimedout is not None:
                if isTimedout['token'] == token:
                    return False
            return True
        except:
            return False

    def is_existing_user(self):
        sql = "SELECT * FROM \"NovelNarrative\".users WHERE \"NovelNarrative\".users.username = {}".format(self.username)
        user_info = self.get_user(sql)
        if user_info is None:
            return False
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)
