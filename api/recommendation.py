import pandas as pd
import joblib
import numpy as np
from database import database

pd.options.display.width = 0


def get_all_predictions_for_user(user_id, data, algorithm, model_type, features, n=10, ):
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
        print(item_ids.size)
        item_ids = item_ids[:-1]
        predictions = algorithm.predict(user_id, item_ids, item_features=features)

        recommendations = data['movieid'][np.argsort(-predictions)]
        recDF = pd.DataFrame(data=recommendations[1:], index=recommendations[1:])
    return recDF.head(n)


def get_book_recommendations(user_id, number_of_recs=10):
    bookData = database.get_all_books()
    bookModel = joblib.load("./RecommenderDump/BookModel")
    bookFeatures = joblib.load("./RecommenderDump/BookFeatures")
    userRecommendations = get_all_predictions_for_user(
        user_id, bookData, bookModel, n=number_of_recs, model_type="book", features=bookFeatures)
    for item_id in userRecommendations['book_id']:
        bookTitle = bookData[bookData['book_id'] == int(item_id)]['title'].values[0]
        print(bookTitle)


def get_movie_recommendations(user_id, number_of_recs=10):
    movieData = database.get_all_movies()
    movieFeatures = joblib.load("./RecommenderDump/MovieFeatures")
    print(repr(movieFeatures))
    movieModel = joblib.load("./RecommenderDump/MovieModel")
    moviesWithFeatures = database.get_movies_with_features(movieData)
    userRecommendations = get_all_predictions_for_user(
        user_id, moviesWithFeatures, movieModel, n=number_of_recs, model_type="movie", features=movieFeatures)
    for item_id in userRecommendations['movieid']:
        movieTitle = movieData[movieData['movieid'] == int(item_id)]['title'].values[0]
        print(movieTitle)
# print(bookData.head())


def main():
    get_movie_recommendations(27)


main()
