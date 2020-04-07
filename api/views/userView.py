from flask import Blueprint, request, jsonify, abort, make_response
from ..models.users import Users
from app import app
import hashlib, binascii, os


@app.route('/register', methods=["POST"])
def user_register():
    try:
        user_data = request.get_json()
        name = user_data['name']
        username = user_data['username']
        password = hash_password(user_data['password'])
        email = user_data['email']
    except Exception as error:
        return jsonify({"error": "invalid user data input",
                        "message": "missing either name, username, email or password",
                        "status": 400
                        }), 400
    new_user = Users([name, username, email, password])
    if ~(new_user.is_existing_user()):
        new_user.create_new_user()
        return jsonify({
            "status": 201,
            "message": "user created successfully"
        }), 201
    return jsonify({"status": 403, "message": "username already exists"}), 403


@app.route('/login', methods=["POST"])
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
    user = Users(['', username, '', password])
    found_user = user.query_login()
    if found_user is not None:
        if verify_password(found_user['password'], password):
            token = user.generate_auth_token()
            return jsonify({
                'user': username, 'token': token.decode('ascii'),
                'message': 'login was successful'}), 200
        else:
            return jsonify({
                'Error': 'Incorrect Password'
            }), 403
    return jsonify({
        'Error': 'Username not found'
    }), 403


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
