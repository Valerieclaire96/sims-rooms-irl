"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Object, Room, Meta
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

def generate_object_list():
    object_list = [
        {
            "name": "namehere",
            "buy_url": "namehere.com",
            "sims_pic_url": "namehere.com",
            "real_pic_url": "namehere.com",
            "price": 9,
        },
        {
            "name": "namehere",
            "buy_url": "namehere.com",
            "sims_pic_url": "namehere.com",
            "real_pic_url": "namehere.com",
            "price": 9,
        },
    ]
    for object in object_list:
        new_object = Object(
            name = object['name'],
            buy_url = object['buy_url'],
            sims_pic_url = object['sims_pic_url'],
            real_pic_url = object['real_pic_url'],
            price = object['price'],
        )
        db.session.add(new_object)
        db.session.commit()


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    generate_object_list()
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/object', methods=['POST'])
def add_object():
    request_body = request.get_json(force=True)
    name = request_body.get("name")
    buy_url = request_body.get("buy_url")
    sims_pic_url = request_body.get("sims_pic_url")
    real_pic_url = request_body.get("real_pic_url")
    price = request_body.get("price")


    return jsonify(response_body), 200

@api.route('/object/str:name>', methods=['GET'])
def get_object(name):
    my_object = Object.query.filter_by(name=name).first()

    return jsonify(my_object), 200

