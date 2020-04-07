import psycopg2
from database import databaseConfig as cfg
import pandas as pd


class DatabaseManager:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user=cfg.postgres['user'],
                                               host=cfg.postgres['host'],
                                               password=cfg.postgres['password'],
                                               port=cfg.postgres['port'],
                                               database=cfg.postgres['database'])
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close_database_connection(self):
        self.connection.close()

    def insert_into_database(self, query):
        self.cursor.execute(query)
        self.connection.commit

    def get_user(self, query):
        user = pd.read_sql_query(query, self.connection)
        return user


    def get_book_ratings(self):
        sql = "SELECT * FROM \"NovelNarrative\".bookratings"
        book_ratings = pd.read_sql_query(sql, self.connection)
        return book_ratings

    def get_movie_ratings(self):
        sql = "SELECT * FROM \"NovelNarrative\".movieratings"
        movie_ratings = pd.read_sql_query(sql, self.connection)
        return movie_ratings

    def get_all_books(self):
        sql = "SELECT * FROM \"NovelNarrative\".books"
        books = pd.read_sql_query(sql, self.connection)
        return books

    def get_book_tags(self):
        sql = "SELECT * FROM \"NovelNarrative\".booktags"
        book_tags = pd.read_sql_query(sql, self.connection)
        return book_tags

    def get_book_tag_desc(self):
        sql = "SELECT * FROM \"NovelNarrative\".booktagsdesc"
        book_tags_desc = pd.read_sql_query(sql, self.connection)
        return book_tags_desc

    def get_book_features(self, books):
        book_tags = self.get_book_tags()
        book_tags_desc = self.get_book_tag_desc()

        book_id_DF = books[['book_id', 'goodreads_book_id']]
        bookTags = book_tags.merge(book_id_DF, on="goodreads_book_id")
        bookTags = bookTags.merge(book_tags_desc, on="tag_id")
        bookFeaturesDF = bookTags[['book_id', 'tag_name']]
        bookFeaturesDF = bookFeaturesDF.dropna()
        return bookFeaturesDF

    def get_all_movies(self):
        sql = "SELECT * FROM \"NovelNarrative\".movies"
        movies = pd.read_sql_query(sql, self.connection)
        return movies

    def get_movie_tags(self):
        sql = "SELECT * FROM \"NovelNarrative\".movietags"
        movie_tags = pd.read_sql_query(sql, self.connection)
        return movie_tags

    def get_movie_features(self, movie_ratings=None):
        movie_tags = self.get_movie_tags()
        if movie_ratings is None:
            movie_ratings = self.get_movie_ratings()
        movie_tags = movie_tags[['movieid', 'tag']]
        movie_features = movie_tags.dropna()
        movie_features = movie_features[movie_features.movieid.isin(movie_ratings.movieid)]
        return movie_features

    def get_movies_with_features(self, movies):
        movie_features = self.get_movie_features()
        movies = movies[movies.movieid.isin(movie_features.movieid)]
        print(movies.head())
        return movies
