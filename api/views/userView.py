import binascii
import hashlib
import os
from flask import request, jsonify, make_response, Blueprint
from models.users import Users


userRoutes = Blueprint('userRoutes', __name__)


def load_user(user_id):
    user = Users(user_data=[user_id, "", "", "", ""])
    return Users.get_user(user, "SELECT * FROM \"NovelNarrative\".users WHERE user_id = ".format(user_id))


@userRoutes.route('/register', methods=["POST"])
def user_register():
    try:
        user_data = request.get_json()
        name = user_data['name']
        username = user_data['username']
        password = hash_password(user_data['password'])
        email = user_data['email']
    except Exception as error:
        return make_response(jsonify({"error": "invalid user data input",
                                      "message": "missing either name, username, email or password",
                                      "status": 400
                                      }), 400)
    new_user = Users([name, username, password, email])
    if not new_user.is_existing_user():
        new_user.create_new_user()
        return make_response(jsonify({
            "status": 201,
            "message": "user created successfully"
        }), 201)
    return make_response(jsonify({"status": 403, "message": "username already exists"}), 403)


@userRoutes.route('/login', methods=["POST"])
def user_login():
    try:
        user_data = request.get_json()
        username = user_data['username']
        password = user_data['password']
    except Exception as error:
        return jsonify({"Error": "Invalid User Input",
                        "message": "missing either username or password",
                        "status": 400
                        }), 400
    user = Users(['', username, password, ''])
    found_user = user.query_login()
    if found_user is not None:
        print(password)
        print(found_user.password)
        if found_user.password == password:
            token = found_user.generate_auth_token()
            return jsonify({
                'user': username, 'token': token['sub'],
                'message': 'login was successful'}), 200
        else:
            return jsonify({
                'Error': 'Incorrect Password'
            }), 403
    return jsonify({
        'Error': 'Username not found'
    }), 403


@userRoutes.route('/logout', methods=['POST'])
def logout():
    try:
        # timed_out = Token(token, date=datetime.utcnow())
        # timed_out.add_token()
        return jsonify({'message': 'Logout success'}), 200
    except Exception as ex:
        return jsonify(ex), 400


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password
