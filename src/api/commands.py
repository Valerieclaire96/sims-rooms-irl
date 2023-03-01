
import click
from api.models import db, User, Room, Object, Meta
import os
import random
from flask import Flask, request, jsonify, url_for
"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_data(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

        ### Insert the code to populate others tables if needed
    @app.cli.command("populate-object-table")
    def generate_object_list():
        object_list = [
            {
                "name": "Architecture art",
                "sims_name": "Roman Temple Architectural study",
                "buy_url": "Architecture Art 4 : 18th C. English Townhouse Collection - Etsy",
                "sims_pic_url": "https://imgur.com/Lmr3ZMq",
                "real_pic_url": "https://i.etsystatic.com/8306577/r/il/b40bb7/3138741932/il_1140xN.3138741932_8jt9.jpg",
                "price": 58,
                "rooms": ["Dude, Where's my Closet?" , "Quick Bites, Long Talks"],
                "meta_tags": ["Classic", "traditional", "farmhouse", "black", "white", "decor", "picture"]
            },
            {
                "name": "lattice rug",
                "sims_name": "Lattice in indoor-outdoor rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/alcott-hill-tylersburg-moroccan-trellis-ivorynavy-area-rug-alth6143.html?piid=25521865%2C38411307",
                "sims_pic_url": "https://imgur.com/SmhGAwI",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/84132909/resize-h1600-w1600%5Ecompr-r85/5860/58602179/Tylersburg+Machine+Woven+%2F+Power+Loomed+Performance+Rug.jpg",
                "price": 170,
                "rooms": ["Dude, Where's my Closet?"],
                "meta_tags": ["simple", "contemporary", "brown", "white", "rug", "decor"]
            },
            {
                "name": "padded headboard",
                "sims_name": "The princess and the pineapple bed",
                "buy_url": "https://a.co/d/6ghdt8J",
                "sims_pic_url": "https://imgur.com/JakzBPi",
                "real_pic_url": "https://m.media-amazon.com/images/I/71WpveLsHmL._AC_SL1500_.jpg",
                "price": 270,
                "rooms": ["Dude, Where's my Closet?"],
                "meta_tags": ["modern", "contemporary", "grey", "bed", "headboard"]
            },
        ]
        for object in object_list:
            new_object = Object(
                name = object['name'],
                sims_name = object['sims_name'],
                buy_url = object['buy_url'],
                sims_pic_url = object['sims_pic_url'],
                real_pic_url = object['real_pic_url'],
                price = object['price'],
            )
            db.session.add(new_object)
            db.session.commit()