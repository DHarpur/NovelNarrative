from flask import request, jsonify, Blueprint
from models.books import Books
from models.users import Users
from authentication import check_token_wrapper
from recommendation import get_book_recommendations

bookRoutes = Blueprint('bookRoutes', __name__)


@bookRoutes.route('/books/rate_books', methods=['POST'])
# @check_token_wrapper
def rate_movies(token):
    try:
        user_id, book_data = Users.decode_token(token), request.get_json()
        for book in book_data:
            bookAttributeList = []
            for attribute, value in book.items:
                bookAttributeList.append(value)
            newRatings = Books(user_id, bookAttributeList[0], bookAttributeList[1])
            newRatings.add_rating()
            # initialiseBookModel()
        return jsonify({'books': book_data, 'message': 'Ratings added'}), 201
    except Exception as ex:
        return jsonify({'Error': ex, 'message': 'Add Ratings failed'}), 400


@bookRoutes.route('/books/recommend/<user_id>', methods=['GET'])
# @check_token_wrapper
def get_recommended_books(user_id, n=20):
    try:
        # user_id = Users.decode_token(token)
        user_recommendations = get_book_recommendations(user_id, n)
        return jsonify(user_recommendations), 200
    except Exception as ex:
        return jsonify({'Error': ex, 'message': 'Get Book recommendations failed'})
