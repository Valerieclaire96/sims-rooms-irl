"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Object, Room, Meta, ObjectPlace, Favorites
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from datetime import datetime, timedelta
import requests
import os 


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
    name = request_body.get('name')

    if not request_body["name"]:
        return jsonify({"msg": "Name is required"}), 400
    if not request_body["email"]:
        return jsonify({"msg": "Email is required"}), 400
    if not request_body["password"]:
        return jsonify({"msg": "Password is required"}), 400

    user = User.query.filter_by(email=email).first()
    if user is not None:
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(email=email, password=password, name=name, is_active=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@api.route('/login', methods=['POST'])
def login():
    request_body = request.get_json()
    email = request_body.get('email')
    password = request_body.get('password')
    print(email, password)
    user = User.query.filter_by(email=email, password=password).first()
    if user is not None:
        expiration = timedelta(days=1)
        access_token = create_access_token(identity= user.id, expires_delta= expiration)
        return jsonify(access_token=access_token, user=user.serialize())

    return jsonify({"message": "User doesn't exists"}), 400

@api.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()

    if user is not None:
        return jsonify(user.serialize()), 200

    return jsonify({"message": "Uh-oh"}), 400

@api.route('/forgot-password', methods=['POST'])
def forgot_password():
    request_body = request.get_json()
    email = request_body.get('email')
    user = User.query.filter_by(email=email).first()
    
    if user is not None:
        expiration = timedelta(days=1)
        access_token = create_access_token(identity= user.id, expires_delta= expiration)
        user_email = user.email
        user_message = "Click this link to change your password: " + "https://3000-valerieclai-simsroomsir-e3rn5q37h3v.ws-us92.gitpod.io/update-password?token=" + str(access_token)
        
        response = requests.post(
		"https://api.mailgun.net/v3/sandboxf995e309d6dc4e28a38a62b293909595.mailgun.org/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": "<sims.irl.pw.recovery@Ysandboxf995e309d6dc4e28a38a62b293909595.mailgun.org>",
			"to": [user_email],
			"subject": "Password recovery",
			"text": user_message})
        return jsonify(status_msg="email sent", user_email=user_email)
    
@api.route('/recover-password', methods=['POST'])
@jwt_required()
def recover_password():
    request_body = request.get_json()
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    password = request_body.get('password')
    
    if user is not None:
        user.password = password
        db.session.commit()
        return jsonify(user.serialize()), 201

@api.route('/object', methods=['POST'])
def add_object():
    request_body = request.get_json(force=True)
    name = request_body.get("name")
    buy_url = request_body.get("buy_url")
    sims_pic_url = request_body.get("sims_pic_url")
    real_pic_url = request_body.get("real_pic_url")
    price = request_body.get("price")
    rooms = request_body.get("room")
    meta_tags = request_body.get("meta_tags")

    return jsonify(request_body), 200


@api.route('/objects', methods=['GET'])
def get_objects():
    room = None
    objects_list = Object.query
    if "name" in request.args:
        objects_list = objects_list.filter(Object.name.ilike(f"%{request.args['name']}%"))
    if "room_id" in request.args:
        objects_list = objects_list.filter(Object.rooms.any(id = request.args['room_id']))
    objects_list = objects_list.all()
    all_objects = list(map(lambda object: object.serialize(), objects_list))
    return jsonify(all_objects), 200

@api.route('/room/<int:room_id>/objects', methods=['GET'])
def get_objects_placement(room_id):
    room = None
    objects_list = ObjectPlace.query.filter_by(room_id = room_id).all()
    all_objects = list(map(lambda object_place: object_place.serialize(), objects_list))
    return jsonify(all_objects), 200

# @api.route('/objects', methods=['GET'])
# def get_objects():
#     objects_list = Object.query.all()
#     all_objects = list(map(lambda object: object.serialize(), objects_list))
#     return jsonify(all_objects), 200

@api.route('/objects/<int:id>', methods=['GET'])
def get_object(id):
    r_object = Object.query.filter_by(id=id).first()
    return jsonify(r_object.serialize()), 200

@api.route('/room', methods=['POST'])
def add_room():
    request_body = request.get_json(force=True)
    name = request_body.get("name")
    pic_url = request_body.get("pic_url")
    objects = request_body.get("objects")
    meta_tags = request_body.get("meta_tag")

    return jsonify(request_body), 200

@api.route('/rooms', methods=['GET'])
def get_rooms():
    rooms_list = Room.query
    if "name" in request.args:
        rooms_list = rooms_list.filter(Room.name.ilike(f"%{request.args['name']}%"))
    rooms_list = rooms_list.all()
    all_rooms = list(map(lambda room: room.serialize(), rooms_list))
    return jsonify(all_rooms), 200


@api.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    room = Room.query.filter_by(id=id).first()
    return jsonify(room.serialize()), 200


# @api.route('/meta', methods=['POST'])
# def add_meta():
#     request_body = request.get_json(force=True)
#     tag = request_body.get("tag")

#     return jsonify(request_body), 200

# @api.route('/metatags', methods=['GET'])
# def get_meta_tags():
#     meta_tags_list = Meta.query
#     if "tag" in request.args:
#         meta_tags_list = meta_tags_list.filter(Meta.tag.ilike(f"%{request.args['tag']}%"))
#     meta_tags_list = meta_tags_list.all()
#     all_meta_tags = list(map(lambda meta_tags: meta_tags.serialize(), meta_tags_list))
#     return jsonify(all_meta_tags), 200


# @api.route('/metatags/<int:id>', methods=['GET'])
# def get_meta_tag(id):
#     meta_tags = Meta.query.filter_by(id=id).first()
#     return jsonify(meta_tags.serialize()), 200



@api.route('/favorites', methods=['POST'])
@jwt_required()
def addFavorite():
  uid = get_jwt_identity()
  request_body = request.get_json()
  #print(request_body)
  favorite = Favorites(
    uid = uid,
    sims_card = repr(request_body['sims_card']),
  )
  
  db.session.add(favorite)   
  db.session.commit()
  # get favorites for logged user
#   favorites = getFavoritesByID(uid)
  #print(favorites)
  # return those favs - same happens in the delete function
  return jsonify(msg="ok")
  
# remove fav----------------------------------------------------------------------------------------------------
@api.route('/deletefav', methods=['DELETE'])
@jwt_required()
def removeFav():
  uid = get_jwt_identity()
  request_body = request.get_json()
  sims_card=repr(request_body['sims_card'])
  Favorites.query.filter_by(
    sims_card=sims_card
    ).delete()
    
  db.session.commit()
  return jsonify(msg="ok")
    
  db.session.commit()
  return jsonify(msg="ok")

# get all fav----------------------------------------------------------------------------------------------------
@api.route('/getfavorites', methods=['GET'])
@jwt_required()
def getFavorites():
  uid = get_jwt_identity()
  user = User.query.filter_by(id=uid).first()

  return jsonify(favorites=user.get_favorites())

