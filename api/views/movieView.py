from flask import request, jsonify, Blueprint
from models.movies import Movies
from models.users import Users
from authentication import check_token_wrapper
from recommendation import get_movie_recommendations
from buildRecommender import initialiseMovieModel

movieRoutes = Blueprint('movieRoutes', __name__)


@movieRoutes.route('/movies/rate_movies', methods=['POST'])
# @check_token_wrapper
def rate_movies(token):
    try:
        user_id, movie_data = Users.decode_token(token), request.get_json()
        for movie in movie_data:
            movieAttributeList = []
            for attribute, value in movie.items:
                movieAttributeList.append(value)
            newRatings = Movies(user_id, movieAttributeList[0], movieAttributeList[1])
            newRatings.add_rating()
            # initialiseMovieModel()
        return jsonify({'movies': movie_data, 'message': 'Ratings added'}), 201
    except Exception as ex:
        return jsonify({'Error': ex, 'message': 'Add Ratings failed'}), 400


@movieRoutes.route('/movies/recommend/<user_id>', methods=['GET'])
# @check_token_wrapper
def get_recommended_movies(user_id, n=20):
    try:
        # user_id = Users.decode_token(token)
        user_recommendations = get_movie_recommendations(user_id, n)
        return jsonify(user_recommendations), 200
    except Exception as ex:
        return jsonify({'Error': ex, 'message': 'Get movie recommendations failed'})
