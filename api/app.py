from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
import recommendation
import buildRecommender
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
bcrypt = Bcrypt(app)

app.secret_key = b'G\x0e\x07\x94\xf3ASGP\xe9\x98\x82\x07[\\\xeeq\xda =\xbf3$*'

loginManager = LoginManager()
loginManager.init_app(app)

@app.route('/login/<username>')


@app.route('/books/recommend/<user_id>', methods=['GET'])
def book_recommend(user_id):
    recommendations = recommendation.get_book_recommendations(user_id)
    recommendations = recommendations.to_json('records')
    return recommendations


@app.route('/movies/recommend/<user_id>', methods=['GET'])
def movie_recommend(user_id):
    recommendations = recommendation.get_movie_recommendations(user_id)
    recommendations = recommendations.to_json('records')
    return recommendations


@app.route('/movies/new_user/', methods=['GET'])
def movie_remake_model():
    buildRecommender.initialiseMovieModel()


@app.route('/books/new_user/', methods=['GET'])
def book_remake_model():
    buildRecommender.initialiseBookModel()

@app.route('/movies/new_ratings/')
def prep_new_ratings():

@app.errorhandler(404)
def not_found(error):
    return {'error': error}, 404


if __name__ == '__main__':
    app.run()
