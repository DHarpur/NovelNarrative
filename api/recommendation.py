import pandas as pd
import joblib
# from app import app
import numpy as np
from flask import jsonify
from database import database

pd.options.display.width = 0


def get_all_predictions_for_user(user_id, data, algorithm, model_type, features, n=10):
    recDF = None
    if model_type == "book":
        item_ids = data['book_id']
        item_ids = item_ids.to_numpy()
        print(item_ids.size)
        item_ids = item_ids[:-1]
        predictions = algorithm.predict(user_id, item_ids, item_features=features)

        recommendations = data['book_id'][np.argsort(-predictions)]
        recDF = pd.DataFrame(data=recommendations[1:], index=recommendations[1:])
    elif model_type == "movie":
        item_ids = data['movieid']
        item_ids = item_ids.to_numpy()
        # item_ids = item_ids.flatten()
        print(item_ids.size)
        predictions = algorithm.predict(user_id, item_ids)

        recommendations = data['movieid'][np.argsort(-predictions)]
        recDF = pd.DataFrame(data=recommendations[1:], index=recommendations[1:])
    return recDF.head(n)


# @app.route('/books/recommendations/<int:user_id>')
def get_book_recommendations(user_id, number_of_recs=10):
    connection = database.DatabaseManager()
    bookData = connection.get_all_books()
    bookModel = joblib.load("./RecommenderDump/BookModel")
    bookFeatures = joblib.load("./RecommenderDump/BookFeatures")
    userRecommendations = get_all_predictions_for_user(
        user_id, bookData, bookModel, n=number_of_recs, model_type="book", features=bookFeatures)
    topRecommendations = []
    for item_id in userRecommendations['book_id']:
        bookTitle = bookData[bookData['book_id'] == int(item_id)]['title'].values[0]
        bookAuthor = bookData[bookData['book_id'] == int(item_id)]['authors'].values[0]
        bookImage = bookData[bookData['book_id'] == int(item_id)]['image_url'].values[0]
        bookDict = {
            "title": bookTitle, "author": bookAuthor, "image": bookImage
        }
        topRecommendations.append(bookDict)
    # print(topRecommendations)
    return topRecommendations


# @app.route('/movies/recommendations/<int:user_id>')
def get_movie_recommendations(user_id, number_of_recs=10):
    connection = database.DatabaseManager()
    movieData = connection.get_all_movies()
    # movieFeatures = joblib.load("./RecommenderDump/MovieFeatures")
    # print(repr(movieFeatures))
    movieModel = joblib.load("./RecommenderDump/MovieModel")
    moviesWithFeatures = connection.get_movies_with_features()
    userRecommendations = get_all_predictions_for_user(
        user_id, movieData, movieModel, n=number_of_recs, model_type="movie", features=None)
    for item_id in userRecommendations['movieid']:
        movieTitle = movieData[movieData['movieid'] == int(item_id)]['title'].values[0]
        print(movieTitle)


def main():
    get_book_recommendations(1755)


# main()
