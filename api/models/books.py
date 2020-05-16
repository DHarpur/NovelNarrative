from database import database


class Books(database.DatabaseManager):
    def __init__(self, book_id, user_id, rating):
        super().__init__()
        self.user_id = user_id
        self.rating = rating
        self.book_id = book_id

    def add_rating(self):

        sql = "INSERT INTO \"NovelNarrative\".bookratings(user_id, book_id, rating) VALUES({}, {}, {})" \
            .format(self.user_id, self.book_id, self.rating)
        self.insert_into_database(sql)