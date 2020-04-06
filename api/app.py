from flask import Flask, jsonify
import recommendation
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/books/recommend/<user_id>', methods=['GET'])
def bookRecommend(user_id):
    recommendations = recommendation.get_book_recommendations(user_id)
    recommendations = recommendations.to_json('records')
    return recommendations


@app.route('/movies/recommend/<user_id>', methods=['GET'])
def movieRecommend(user_id):
    recommendations = recommendation.get_movie_recommendations(user_id)
    recommendations = recommendations.to_json('records')
    return recommendations


app.run()
