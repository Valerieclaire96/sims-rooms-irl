"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Object, Room, Meta
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
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

    return jsonify(request_body), 200


@api.route('/object/<string:object_name>', methods=['GET'])
def get_object(object_name):
    request_body = request.get_json(force=True)
    object_name = request_body.get("object_name")
    object = Object.query.filter_by(name=object_name).first()

    return jsonify(object.serialize()), 200
