from database import database


class Token(database.DatabaseManager):
    def __init__(self, token, date):
        super().__init__()
        self.token = token
        self.date = date

    def add_token(self):
        sql = "INSERT INTO \"NovelNarrative\".auth_token(token, date) VALUES '{}', '{}'".format(self.token, self.date)
        self.insert_into_database(sql)
