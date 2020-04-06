import psycopg2
from database import databaseConfig as cfg
import pandas as pd


def get_book_ratings():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".bookratings"
        book_ratings = pd.read_sql_query(sql, connection)
        return book_ratings
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_movie_ratings():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".movieratings"
        movie_ratings = pd.read_sql_query(sql, connection)
        return movie_ratings
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_all_books():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".books"
        books = pd.read_sql_query(sql, connection)
        return books
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_book_tags():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".booktags"
        book_tags = pd.read_sql_query(sql, connection)
        return book_tags
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_book_tag_desc():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".booktagsdesc"
        book_tags_desc = pd.read_sql_query(sql, connection)
        return book_tags_desc
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_book_features(books):
    book_tags = get_book_tags()
    book_tags_desc = get_book_tag_desc()

    book_id_DF = books[['book_id', 'goodreads_book_id']]
    bookTags = book_tags.merge(book_id_DF, on="goodreads_book_id")
    bookTags = bookTags.merge(book_tags_desc, on="tag_id")
    bookFeaturesDF = bookTags[['book_id', 'tag_name']]
    bookFeaturesDF = bookFeaturesDF.dropna()
    return bookFeaturesDF


def get_all_movies():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".movies"
        movies = pd.read_sql_query(sql, connection)
        return movies
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_movie_tags():
    connection = None
    try:
        connection = psycopg2.connect(user=cfg.postgres['user'],
                                      host=cfg.postgres['host'],
                                      password=cfg.postgres['password'],
                                      port=cfg.postgres['port'],
                                      database=cfg.postgres['database'])
        sql = "SELECT * FROM \"NovelNarrative\".movietags"
        movie_tags = pd.read_sql_query(sql, connection)
        return movie_tags
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_movie_features(movie_ratings):
    movie_tags = get_movie_tags()
    movie_tags = movie_tags[['movieid', 'tag']]
    movie_features = movie_tags.dropna()
    movie_ratings = movie_ratings['movieid']
    movie_feature_ids = movie_features['movieid']
    movies_to_remove = (~(movie_feature_ids.isin(movie_ratings))).index
    movie_features.drop(movies_to_remove, inplace=True)
    return movie_features


def get_movies_with_features(movies):
    movie_tags = get_movie_tags()
    movie_tags = movie_tags[['movieid', 'tag']]
    movie_features = movie_tags.dropna()
    movie_feature_ids = movie_features['movieid']
    # movies_to_remove = (~movieIds.isin(movie_feature_ids)).index
    # movies = movies[movies.movieid.isin(movie_feature_ids)]
    # movies.drop(movies_to_remove, inplace=True)
    print(movies.head())
    return movies
