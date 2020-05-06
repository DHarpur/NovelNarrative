from database import database
import time


class Movies(database.DatabaseManager):
    def __init__(self, user_id, tmdmovie_id, rating):
        super().__init__()
        self.user_id = user_id
        self.tmdmovie_id = tmdmovie_id
        self.rating = rating
        self.movie_id = None
        self.timestamp = None

    def get_movie_id(self):
        sql = "SELECT movieid FROM \"NovelNarrative\".movielinks WHERE \"NovelNarrative\".movielinks.tmdbid = {}"\
            .format(self.tmdmovie_id)
        self.movie_id = self.get_movie(sql)

    def add_rating(self):
        self.timestamp = time.time()
        self.get_movie_id()
        sql = "INSERT INTO \"NovelNarrative\".movieratings(userid, movieid, rating, timestamp) VALUES({}, {}, {}, {})"\
            .format(self.user_id, self.movie_id, self.rating, self.timestamp)
        self.insert_into_database(sql)
