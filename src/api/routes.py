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
            "name": "Roman Temple Architectural study",
            "buy_url": "Architecture Art 4 : 18th C. English Townhouse Collection - Etsy",
            "sims_pic_url": "https://imgur.com/Lmr3ZMq",
            "real_pic_url": "https://i.etsystatic.com/8306577/r/il/b40bb7/3138741932/il_1140xN.3138741932_8jt9.jpg",
            "price": 58,
        },
        {
            "name": "Lattice in indoor-outdoor rug",
            "buy_url": "https://www.wayfair.com/rugs/pdp/alcott-hill-tylersburg-moroccan-trellis-ivorynavy-area-rug-alth6143.html?piid=25521865%2C38411307",
            "sims_pic_url": "https://imgur.com/SmhGAwI",
            "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/84132909/resize-h1600-w1600%5Ecompr-r85/5860/58602179/Tylersburg+Machine+Woven+%2F+Power+Loomed+Performance+Rug.jpg",
            "price": 170,
        },
        {
            "name": "The princess and the pineapple bed",
            "buy_url": "https://a.co/d/6ghdt8J",
            "sims_pic_url": "https://imgur.com/JakzBPi",
            "real_pic_url": "https://m.media-amazon.com/images/I/71WpveLsHmL._AC_SL1500_.jpg",
            "price": 270,
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
        db.commit()


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

