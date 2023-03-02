
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

    @app.cli.command("populate-room-table")
    def generate_room_list():
        room_list = [
            {
                "name": "Dude, Where's my Closet?",
                "pic_url": "https://imgur.com/SmhGAwI",
                "objects": ["architecture art" , "lattice rug", "padded headboard", "salt lamp", "dog planter", "clothing rack", "wicker hamper"],
                "meta_tags": ["contemporary", "modern", "minimalist", "simple", "bedroom"]
            },
             {
                "name": "geeks4Sleep",
                "pic_url": "https://imgur.com/MT1HV5j",
                "objects":  ["indstrial lamp", "gaming chair", "gaming desk", "checkered rug", "record art", "round table", "wardrobe","bamboo","lava lamp"],
                "meta_tags": ["teen", "contemporary", "bedroom", "black"]
            },
             {
                "name": "Lazy Susan’s Kitchen",
                "pic_url": "https://i.imgur.com/9WdnFoR.png",
                "objects":  ["stripped planter" ,"pet feeder", "popcorn maker", "dutch oven", "barstool", "tea rack", "knife rack"],
                "meta_tags": ["architecture art" , "lattice rug", "padded headboard", "salt lamp", "dog planter", "clothing rack", "wicker hamper"]
            },
             {
                "name": "Quick Bites, Long Talks",
                "pic_url": "https://i.imgur.com/tPG1Meg.png",
                "objects": ["mc dining table", "mc console table", "floor lamp", "md dining chair", "architecture art", "lotus candle"],
                "meta_tags": ["mid century modern", "modern", "contemporary","dining room", "vintage", "scandinavian"]
            },
             {
                "name": "The Fancy Man’s Study",
                "pic_url": "https://i.imgur.com/tPG1Meg.png",
                "objects":  ["studded arm chair", "globe bar", "bankers lamp", "Persian rug", "executive desk chair", "executive desk"],
                "meta_tags":  ["office", "study", "classic", "traditional","brown","wood"]
            },
             {
                "name": "Straight As to Zzz",
                "pic_url": "https://i.imgur.com/YpAijUT.png",
                "objects": ["leaf art", "mirror with lights", "director’s chair", "white gold dresser", "salt lamp"],
                "meta_tags":  ["teen", "contemporary","modern","chic","luxe","glamor","bedroom"]

            },
             {
                "name": "Tweenage Dirtbag",
                "pic_url": "https://imgur.com/HHILH8C",
                "objects": ["pink floyd poster","nautro rug","desk lamp","rice paper lamp","bean bag","bunk bed"],
                "meta_tags": ["kid","teen","contemporary", "bedroom","white","blue"]
            },
             {
                "name": "Unicorn Dreams",
                "pic_url": "https://imgur.com/iaJefXz",
                "objects": ["wall decal","teddy bear","unicorn","butterfly chair","house toddler bed","string lights","rolling car pink"],
                "meta_tags": ["kids","cute","pink","purple"]
            },
             {
                "name": "Vroom Room",
                "pic_url": "https://imgur.com/2W36O5V",
                "objects": ["school bus toybox","blue rug","dragon","rolling cart","racecar bed","panda chair"],
                "meta_tags": ["kids","cute","blue"]
            },
             {
                "name": "Zen Den",
                "pic_url": "https://i.imgur.com/6aHMhet.png",
                "objects": ["cat planter","lotus candle","arc lamp","wicker basket","handing planter","noddle candle","moroccan rug","blue sofa","console table","industrial coffee table"],
                "meta_tags": ["boho", "eclectic", "bohemian", "shabby chic", "living room"] 
            },
        ]
        for room in room_list:
            new_room = Room(
                name = room['name'],
                sims_name = room['sims_name'],
                pic_url = room['pic_url'],
                real_pic_url = room['real_pic_url'],
                objects = room['objects'],
                meta_tags = room['meta_tags']
            )
            db.session.add(new_room)
            db.session.commit()

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
                rooms = object['rooms'],
                meta_tags = object['meta_tags']
            )
            db.session.add(new_object)
            db.session.commit()

    @app.cli.command("populate-meta-table")
    def generate_meta_list():
        meta_list = [
            {
                "description" : "kids"
            },
            {
                "description" : "wood"
            },
            {
                "description" : "kitchen"
            },
        ]
        for object in object_list:
            new_description = Meta(
                description = object['description']
            )
            db.session.add(new_description)
            db.session.commit()