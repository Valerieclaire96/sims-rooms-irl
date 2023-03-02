"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Object, Room, Meta
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def create_account():
    request_body = request.get_json()
    email = request_body.get('email')
    password = request_body.get('password')
    profile_pic = request_body.get('profile_pic')

    user = User.query.filter_by(email=email).first()
    if user is not None:
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(email=email, password=password, profile_pic=profile_pic, is_active=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@api.route('/login', methods=['POST'])
def login():
    request_body = request.get_json()
    email = request_body.get('email')
    password = request_body.get('password')

    user = User.query.filter_by(email=email).first()
    if user is not None:
        token = create_access_token(identity=email)
        return jsonify({'message': 'Successful Sign in', "token": str(token) }), 200
    return jsonify({"message': 'User doesn't exists"}), 400

@api.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    email = get_jwt_identity()
    user = User.query.filter_by(email=email).first()

    if user is not None:
        return jsonify(user.serialize()), 200

    return jsonify({"message": "Uh-oh"}), 400


@api.route('/object', methods=['POST'])
def add_object():
    request_body = request.get_json(force=True)
    name = request_body.get("name")
    buy_url = request_body.get("buy_url")
    sims_pic_url = request_body.get("sims_pic_url")
    real_pic_url = request_body.get("real_pic_url")
    price = request_body.get("price")

    return jsonify(request_body), 200


@api.route('/object/<string:object_name>', methods=['GET'])
def get_object(object_name):
    request_body = request.get_json(force=True)
    object_name = request_body.get("object_name")
    object = Object.query.filter_by(name=object_name).first()

    return jsonify(object.serialize()), 200
