import psycopg2
from database import databaseConfig as config
import pandas as pd


class DatabaseManager:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user=config.postgres['user'],
                                               host=config.postgres['host'],
                                               password=config.postgres['password'],
                                               port=config.postgres['port'],
                                               database=config.postgres['database'])
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close_database_connection(self):
        self.connection.close()

    def insert_into_database(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def get_user(self, query):
        try:
            user = pd.read_sql_query(query, self.connection)
            return user
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_movie(self, query):
        movie = pd.read_sql_query(query, self.connection)
        return movie

    def get_book(self, query):
        book = pd.read_sql_query(query, self.connection)
        return book

    def get_token(self, query):
        token = pd.read_sql_query(query, self.connection)
        return token

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
        sql = "SELECT * FROM \"NovelNarrative\".movietags mt WHERE mt.movieid IN " \
                "(SELECT mr.movieid FROM \"NovelNarrative\".movieratings mr)"
        movie_tags = pd.read_sql_query(sql, self.connection)
        return movie_tags[['movieid', 'tag']]

    def get_movies_with_features(self):
        sql = "SELECT movieid FROM \"NovelNarrative\".movies mt WHERE mt.movieid IN " \
              "(SELECT mr.movieid FROM \"NovelNarrative\".movieratings mr)"
        movies = pd.read_sql_query(sql, self.connection)
        movies = movies['movieid'].unique()
        return movies
