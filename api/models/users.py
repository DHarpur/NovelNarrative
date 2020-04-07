from database import database
import psycopg2
from datetime import datetime, timedelta
import jwt
from app import secret_key

class Users(database.DatabaseManager):
    def __init__(self, user_data, isAdmin=False):
        super().__init__()
        self.user_id = None
        self.name = user_data[0]
        self.username = user_data[1]
        self.email = user_data[2]
        self.password = user_data[3]
        self.isAdmin = isAdmin

    def create_new_user(self):
        sql = "INSERT INTO users(name, username, email, password, isAdmin)" \
              " VALUES( '{}', '{}','{}', '{}', '{}')".format(self.name, self.username, self.email,
                                                             self.password, self.isAdmin)
        self.insert_into_database(sql)

    def query_login(self):
        sql = "SELECT * FROM users WHERE users.username = {}".format(self.username)
        user_info = self.get_user(sql)
        self.user_id = user_info['user_id']
        return user_info

    def generate_auth_token(self, expiration=60000):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=expiration),
                'iat': datetime.utcnow(),
                'sub': self.user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
            return jwt_string
        except Exception as ex:
            raise Exception(ex)

    def is_existing_user(self):
        sql = "SELECT * FROM users WHERE users.username = {}".format(self.username)
        user_info = self.get_user(sql)
        if user_info is None:
            return False
        return True
