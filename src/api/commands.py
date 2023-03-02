
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
                "price": 270,
                "rooms": ["Dude, Where's my Closet?"],
                "meta_tags": ["simple", "contemporary", "brown", "white", "rug", "decor"]
            },
            {
                "name": "padded headboard",
                "sims_name": "The princess and the pineapple bed",
                "buy_url": "https://a.co/d/6ghdt8J",
                "sims_pic_url": "https://imgur.com/JakzBPi",
                "real_pic_url": "https://m.media-amazon.com/images/I/71WpveLsHmL._AC_SL1500_.jpg",
                "price": 170,
                "rooms": ["Dude, where's my closet?"],
                "meta_tags": ["Modern", "Simple", "minimalist"]
            },
            {
                "name": "salt lamp",
                "sims_name": "Lamp finds a way",
                "buy_url": "https://a.co/d/daqgHzX",
                "sims_pic_url": "https://imgur.com/hiPfwrw",
                "real_pic_url": "https://m.media-amazon.com/images/I/612+MvvNgiL._AC_SL1500_.jpg",
                "price": 23,
                "rooms": ["Dude, where's my closet?","Straight as to Zzz"],
                "meta_tags": ["Boho", "rustic", "Eclectic", "orange", "wood", "lamp", "decor"]
            },
            {
                "name": "dog planter",
                "sims_name": "Puppulent succulent",
                "buy_url": "https://a.co/d/1Lyzk8H",
                "sims_pic_url": "https://imgur.com/qmrGR5q",
                "real_pic_url": "https://m.media-amazon.com/images/I/61yj2yUTvFL._AC_SL1001_.jpg",
                "price": 22,
                "rooms": ["Dude, where's my closet?"],
                "meta_tags": ["Cute", "plant", "Eclectic", "plant", "pot", "black", "white", "brown", "green", "multicolor"]
            },
            {
                "name": "clothing rack",
                "sims_name": "Backstreet clothing rack",
                "buy_url": "https://a.co/d/fWys2of",
                "sims_pic_url": "https://imgur.com/zPjohe7",
                "real_pic_url": "https://m.media-amazon.com/images/I/810YHmx21YL._AC_SL1500_.jpg",
                "price": 110,
                "rooms": ["Dude, where's my closet?"],
                "meta_tags": ["Contemporary", "minimalist", "chic", "black", "wood", "dresser", "clothing", "rack"]
            },
            {
                "name": "wicker hamper",
                "sims_name": "Wicker whims hamper",
                "buy_url": "https://a.co/d/epKkUWd",
                "sims_pic_url": "https://imgur.com/pxe6Lsa",
                "real_pic_url": "https://m.media-amazon.com/images/I/A1uwIeK-FfL._AC_SL1500_.jpg",
                "price": 115,
                "rooms": ["Dude, where's my closet?"],
                "meta_tags": ["farmhouse", "rustic", "wood", "brown", "hamper", "laundry", "basket"]
            },
            {
                "name": "industrial lamp",
                "sims_name": "Totality tripod floor lamp",
                "buy_url": "https://a.co/d/fVWdzCz",
                "sims_pic_url": "https://imgur.com/aoWOTkb",
                "real_pic_url": "https://m.media-amazon.com/images/I/71QjFE+tq-L._AC_SL1500_.jpg",
                "price": 49,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["Industrial", "Eclectic", "black", "silver", "lamp", "teen"]
            },
            {
                "name": "gaming chair",
                "sims_name": "Multitasker G",
                "buy_url": "https://a.co/d/0GeMmvK",
                "sims_pic_url": "https://imgur.com/UoIPr7e",
                "real_pic_url": "https://m.media-amazon.com/images/I/612r4sw1jYL._AC_SL1500_.jpg",
                "price": 180,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["teen", "contemporary", "teen", "chair", "desk chair", "gaming chair", "black", "purple", "gaming"]
            },
            {
                "name": "gaming desk",
                "sims_name": "Pr-0 Gaming Desk",
                "buy_url": "https://a.co/d/6ihji1E",
                "sims_pic_url": "https://imgur.com/dAZrqCr",
                "real_pic_url": "https://m.media-amazon.com/images/I/612r4sw1jYL._AC_SL1500_.jpg",
                "price": 158,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["teen", "contemporary", "teen", "black", "multcolor", "rainbow", "desk", "gaming"]
            },
            {
                "name": "checkered rug",
                "sims_name": "Choose your aesthetic rug",
                "buy_url": "https://a.co/d/gN23z9d",
                "sims_pic_url": "https://imgur.com/MT1HV5j",
                "real_pic_url": "https://m.media-amazon.com/images/I/91Lq6XCHLpL._AC_SL1500_.jpg",
                "price": 92,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["teen", "contemporary", "rug", "checkered", "black", "white"]
            },
            {
                "name": "record art",
                "sims_name": "Free association collages",
                "buy_url": "https://a.co/d/bSoP5fq",
                "sims_pic_url": "https://imgur.com/O3kqb2S",
                "real_pic_url": "https://m.media-amazon.com/images/I/91OUnFry9bL._AC_SX466_.jpg",
                "price": 19,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["boho", "teen", "decor", "art", "rainbow", "multi", "black", "vintage"]
            },
            {
                "name": "round table",
                "sims_name": "Sir cumference coffee table",
                "buy_url": "https://a.co/d/89X9h0S",
                "sims_pic_url": "https://imgur.com/NWCjOxa",
                "real_pic_url": "https://m.media-amazon.com/images/I/717q7wg1ZhL._AC_SL1500_.jpg",
                "price": 34,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["modern", "teen", "minimalist", "chic", "table", "coffee table", "side table", "night stand", "contemporary", "black", "circle"]
            },
            {
                "name": "wardrobe",
                "sims_name": "night before dresser",
                "buy_url": "https://a.co/d/iCAD4AE",
                "sims_pic_url": "https://i.imgur.com/hcnNmZ1.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/51TXvzE-mCL._AC_.jpg",
                "price": 255,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["teen", "contemporary", "storage", "dresser", "wardrobe", "wood", "brown", "expresso"]
            },
            {
                "name": "bamboo",
                "sims_name": "Palliatiude Potted bamboo",
                "buy_url": "https://a.co/d/ee6j2Y0",
                "sims_pic_url": "https://imgur.com/fWQxBXu",
                "real_pic_url": "https://m.media-amazon.com/images/I/81M46m8NvfL._AC_SL1500_.jpg",
                "price": 78,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["modern", "chic", "boho", "contemporary", "teen", "green", "black", "plant" ]
            },
            {
                "name": "lava lamp",
                "sims_name": "The green Lava Beacon",
                "buy_url": "https://a.co/d/8eIgrQu",
                "sims_pic_url": "https://imgur.com/NWCjOxa",
                "real_pic_url": "https://m.media-amazon.com/images/I/61dmJx+pZyL._AC_SL1500_.jpg",
                "price": 22,
                "rooms": ["geeks4sleep"],
                "meta_tags": ["retro", "vintage", "green", "atomic", "lamp", "decor"]
            },
            {
                "name": "stripped planter",
                "sims_name": "Faustus the ZZ plant",
                "buy_url": "https://a.co/d/hbOIGve",
                "sims_pic_url": "https://i.imgur.com/LNCop8r.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/612yDwcfJKL._AC_SL1500_.jpg",
                "price": 25,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["modern" "glam", "luxe", "minimalist", "grey", "white", "gold", "planter"]
            },
            {
                "name": "pet feeder",
                "sims_name": "permate programmatic pet feeder",
                "buy_url": "https://a.co/d/7ggdgBh",
                "sims_pic_url": "https://i.imgur.com/lb0PNzQ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/51N593Uu05L._AC_SL1500_.jpg",
                "price": 70,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["pets", "black", "tech", "pet", "feeder", "modern", "minimalist" ]
            },
            {
                "name": "popcorn maker",
                "sims_name": "sugar corn popcorn popper",
                "buy_url": "https://a.co/d/0pRVdSz",
                "sims_pic_url": "https://i.imgur.com/BwIWcRY.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71eZwHSWsjL._AC_SL1500_.jpg",
                "price": 25,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["tech", "applicance", "red" ]
            },
            {
                "name": "dutch oven",
                "sims_name": "the king's cookware- by The Medlin Forge",
                "buy_url": "https://a.co/d/8tUe7mz",
                "sims_pic_url": "https://i.imgur.com/FLhNqne.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81MdPE8Q-4L._AC_SL1500_.jpg",
                "price": 50,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["classic", "farmhouse", "rustic", "red", "cookware"]
            },
            {
                "name": "barstool",
                "sims_name": "The celestial",
                "buy_url": "https://a.co/d/13KAHNk",
                "sims_pic_url": "https://i.imgur.com/Fl4mF8E.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71PAf6HAJyS._AC_SL1500_.jpg",
                "price": 85,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["mid century modern", "atomic", "chic", "mordern", "red", "stool", "bar stool", "swivle"]
            },
            {
                "name": "tea rack",
                "sims_name": "simergy tea sensations",
                "buy_url": "https://a.co/d/81cVZXA",
                "sims_pic_url": "https://i.imgur.com/mGmroRT.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71NzBFARuQL._AC_SL1500_.jpg",
                "price": 23,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["contemporary", "decor", "storage", "wood", "black"]
            },
            {
                "name": "knife rack",
                "sims_name": "positronic pro magnetic knife rack",
                "buy_url": "https://a.co/d/giDUhto",
                "sims_pic_url": "https://i.imgur.com/6FDZkiQ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/41ztJBWqD-L._AC_.jpg",
                "price": 23,
                "rooms": ["Lazy Susan's Kitchen"],
                "meta_tags": ["modern", "industrial", "contemporary", "silver", "decor", "storage"]
            },
            {
                "name": "mc dining table",
                "sims_name": "all of the things table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/wade-logan-agla-hallway-console-table-w000364723.html",
                "sims_pic_url": "https://i.imgur.com/RxOkVfY.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/93954241/resize-h755-w755%5Ecompr-r85/3492/34928790/Agla+40%27%27+Solid+Wood+Console+Table.jpg",
                "price": 350,
                "rooms": ["Quick Bites, Long Talks"],
                "meta_tags": ["mid", "century", "modern", "modern", "contemporary", "Scandinavian", "table", "dining table", "wood", "glass"]
            },
            {
                "name": "mc console table",
                "sims_name": "moder mid-century marvel",
                "buy_url": "https://www.wayfair.com/furniture/pdp/birch-lane-geoff-glass-dining-table-w008599694.html",
                "sims_pic_url": "https://i.imgur.com/EeNoQ2R.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/38840974/resize-h1600-w1600%5Ecompr-r85/2326/232656119/Geoff+43.3%27%27+Dining+Table.jpg",
                "price": 250,
                "rooms": ["quick bites, long talks"],
                "meta_tags": ["mid", "century", "modern", "modern", "contemporary", "Scandinavian"]
            },
            {
                "name": "floor lamp",
                "sims_name": "Not all included' Lamp without storage",
                "buy_url": "https://a.co/d/0jjtRvy",
                "sims_pic_url": "https://i.imgur.com/dZea7Oz.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81wgW-40KxL._AC_SL1500_.jpg",
                "price": 170,
                "rooms": ["quick bites, long talks"],
                "meta_tags": ["mid century modern", "modern", "scandinavian", "wood", "black", "lamp", "decor"]
            },
            {
                "name": "mc dining chair",
                "sims_name": "The Trendsitter",
                "buy_url": "https://a.co/d/5XnHCDE",
                "sims_pic_url": "https://i.imgur.com/E361OMJ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71zYPalXIwL._AC_SL1500_.jpg",
                "price": 300,
                "rooms": ["quick bites, long talks"],
                "meta_tags": ["mid", "century", "modern", "chair", "dining chair", "wood", "retro"]
            },
            {
                "name": "studded arm chair",
                "sims_name": "executive guest chair",
                "buy_url": "https://a.co/d/8cEOsm4",
                "sims_pic_url": "https://imgur.com/RWKMMIc",
                "real_pic_url": "https://m.media-amazon.com/images/I/71NK46jk6lL._AC_SL1500_.jpg",
                "price": 180,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "traditional", "black", "gold", "chair", "arm chair"]
            },
            {
                "name": "globe bar",
                "sims_name": "16th century monte vista globe bar ",
                "buy_url": "https://a.co/d/9CFZr8n",
                "sims_pic_url": "https://imgur.com/uML6YY1",
                "real_pic_url": "https://m.media-amazon.com/images/I/A1+Zq-qJoDL._AC_SL1500_.jpg",
                "price": 170,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "traditional",  "brown", "gold", "black", "bar"]
            },
            {
                "name": "bankers lamp",
                "sims_name": "The artisan",
                "buy_url": "https://a.co/d/a2gD9WC",
                "sims_pic_url": "https://imgur.com/rtiTdQq",
                "real_pic_url": "https://m.media-amazon.com/images/I/71-8Kce+v2S._AC_SX679_.jpg",
                "price": 50,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "traditional", "gold", "green", "lamp"]
            },
            {
                "name": "persian rug",
                "sims_name": "threads of fortune rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/langley-street-edens-oriental-burgundy-area-rug-w004775928.html?piid=1606445080",
                "sims_pic_url": "https://imgur.com/jG5GOPd",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/07880182/resize-h755-w755%5Ecompr-r85/9762/97620517/Edens+Machine+Woven+%2F+Power+Loomed+Performance+Burgundy+Rug.jpg",
                "price": 180,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "persian", "red", "blue", "multi", "rug", "decor"]
            },
            {
                "name": "executive desk chair",
                "sims_name": "executron executive desk throne",
                "buy_url": "https://www.wayfair.com/furniture/pdp/lark-manor-murphie-high-back-traditional-tufted-leathersoft-executive-swivel-ergonomic-office-chair-w001944761.html?piid%5B0%5D=933975933",
                "sims_pic_url": "https://imgur.com/JPUugQj",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/10739145/resize-h755-w755%5Ecompr-r85/1933/193366503/Murphie+High+Back+Traditional+Tufted+LeatherSoft+Executive+Swivel+Ergonomic+Office+Chair.jpg",
                "price": 520,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "traditional", "black", "gold", "chair", "desk chair" ]
            },
            {
                "name": "executive desk",
                "sims_name": "very impressive lawyer-y desk",
                "buy_url": "Hekman 72'' Desk | Wayfair",
                "sims_pic_url": "https://imgur.com/fdf1RFJ",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/15056160/resize-h755-w755%5Ecompr-r85/1047/104759591/72%27%27+Desk.jpg",
                "price": 3,998,
                "rooms": ["The Fancy Man's Study"],
                "meta_tags": ["classic", "traditional", "wood", "brown", "desk"]
            },
            {
                "name": "leaf art",
                "sims_name": "Simple and Clean art",
                "buy_url": "https://a.co/d/8tjebEh",
                "sims_pic_url": "https://i.imgur.com/493s267.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81ZlycohRdL._AC_SL1500_.jpg",
                "price": 30,
                "rooms": ["Straight As to Zzz"],
                "meta_tags": ["teen", "contemporary", "art", "decor", "white", "green", "picture"]
            },
            {
                "name": "mirror with lights",
                "sims_name": "Fit full length vanity mirror",
                "buy_url": "https://a.co/d/16aFJCB",
                "sims_pic_url": "https://i.imgur.com/43Tnda1.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71Ht6+RY-qL._AC_SL1200_.jpg",
                "price": 106,
                "rooms": ["Straight As to Zzz"],
                "meta_tags": ["teen", "contemporary", "white", "glam", "mirror", "lighting"]
            },
            {
                "name": "directors chair",
                "sims_name": "Just a finch directors chair",
                "buy_url": "https://a.co/d/8tRdkuW",
                "sims_pic_url": "https://i.imgur.com/reKadqx.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/91I9mjcPpeL._AC_SL1500_.jpg",
                "price": 93,
                "rooms": ["Straight As to Zzz"],
                "meta_tags": ["teen", "contemporary", "Eclectic", "chair", "white"]
            },
            {
                "name": "white gold dresser",
                "sims_name": "Perplexed dresser",
                "buy_url": "https://a.co/d/e0zYoV6",
                "sims_pic_url": "https://i.imgur.com/YywYqrv.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71TRhy+wLlL._AC_SL1500_.jpg",
                "price": 220,
                "rooms": ["Straight As to Zzz"],
                "meta_tags": ["teen", "modern", "chic", "white", "gold", "glam", "dresser", "storage"]
            },
            {
                "name": "pink floyd poster",
                "sims_name": "Hey I like that poster too",
                "buy_url": "https://a.co/d/3etkW4s",
                "sims_pic_url": "https://imgur.com/DWyyeQM",
                "real_pic_url": "https://m.media-amazon.com/images/I/31By9mlOVLL._AC_.jpg",
                "price": 12,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["retro", "vintage", "black", "multi", "rainbow", "poster", "decor", "kid", "teen"]
            },
            {
                "name": "naruto rug",
                "sims_name": "Reliable rug",
                "buy_url": "https://a.co/d/aZW7zSv",
                "sims_pic_url": "https://imgur.com/HHILH8C",
                "real_pic_url": "https://m.media-amazon.com/images/I/61MXoRUAi-L._AC_SL1500_.jpg",
                "price": 33,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["kid", "teen", "black", "red", "decor", "rug", "teen", "kid"]
            },
            {
                "name": "desk lamp",
                "sims_name": "Lex light by desk pix",
                "buy_url": "https://a.co/d/0xvIyyU",
                "sims_pic_url": "https://imgur.com/YPVZA0l",
                "real_pic_url": "https://m.media-amazon.com/images/I/61R7hBIB0jL._AC_SL1500_.jpg",
                "price": 50,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["Contemporary", "blue", "wood", "lamp"]
            },
            {
                "name": "rice paper lamp",
                "sims_name": "You've got the light",
                "buy_url": "https://a.co/d/dfaU8Nv",
                "sims_pic_url": "https://imgur.com/6wtNhm3",
                "real_pic_url": "https://m.media-amazon.com/images/I/71nP6CvGTAL._AC_SL1500_.jpg",
                "price": 60,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["Contemporary", "modern", "black", "white", "lamp", "teen", "kid"]
            },
            {
                "name": "bean bag",
                "sims_name": "Chair of many colors",
                "buy_url": "https://a.co/d/0M83Iwa",
                "sims_pic_url": "https://imgur.com/i0yK226",
                "real_pic_url": "https://m.media-amazon.com/images/I/41OYjcpRr4L._AC_.jpg",
                "price": 17,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["kid", "teen", "black", "chair" ]
            },
            {
                "name": "bunk bed",
                "sims_name": "Metal fame top bunk",
                "buy_url": "https://a.co/d/8hZDNyl",
                "sims_pic_url": "https://imgur.com/VygFyk8",
                "real_pic_url": "https://m.media-amazon.com/images/I/71e8EANp6ML._AC_SL1500_.jpg",
                "price": 210,
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["Kid", "teen", "black", "bed" ]
            },
            {
                "name": "wall decal",
                "sims_name": "Floating away",
                "buy_url": "https://a.co/d/fMJOxL9",
                "sims_pic_url": "https://imgur.com/x87KkeL",
                "real_pic_url": "https://m.media-amazon.com/images/I/71HBJNvLPwS._AC_SL1300_.jpg",
                "price": 12,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["kid" "cute" "decal" "decor" "multi" "pink" "purple"]
            },
            {
                "name": "teddy bear",
                "sims_name": "The lots of love bear",
                "buy_url": "https://a.co/d/dfSs6jS",
                "sims_pic_url": "https://imgur.com/3TMfnyS",
                "real_pic_url": "https://m.media-amazon.com/images/I/51FSfBMPzXL._AC_SL1000_.jpg",
                "price": 15,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["kid", "cute", "pink", "red", "toy" ]
            },
            {
                "name": "unicorn",
                "sims_name": "Uni",
                "buy_url": "https://a.co/d/b181DG1",
                "sims_pic_url": "https://imgur.com/LNPgEbX",
                "real_pic_url": "https://m.media-amazon.com/images/I/71f0m-0-t5L._AC_SX425_.jpg",
                "price": 70,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["kid", "cute", "pink", "purple", "toy"]
            },
            {
                "name": "butterfly chair",
                "sims_name": "The Gordian spritz",
                "buy_url": "https://a.co/d/2uTy8cP",
                "sims_pic_url": "https://imgur.com/C3DySEs",
                "real_pic_url": "https://m.media-amazon.com/images/I/710NuDZK2FL._AC_SL1500_.jpg",
                "price": 20,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["kid", "cute", "pink", "blue", "chair"]
            },
            {
                "name": "house toddler bed",
                "sims_name": "The freezepop sleep spot",
                "buy_url": "https://a.co/d/h4Iz4c2",
                "sims_pic_url": "https://imgur.com/ePPYIWK",
                "real_pic_url": "https://m.media-amazon.com/images/I/71fQae7TEjL._AC_SL1500_.jpg",
                "price": 310,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["kid", "cute", "white", "bed", "toddler bed"]
            },
            {
                "name": "string lights",
                "sims_name": "Say Good night little lights",
                "buy_url": "https://a.co/d/5HQuT26",
                "sims_pic_url": "https://imgur.com/OwbrUao",
                "real_pic_url": "https://m.media-amazon.com/images/I/61kNKty4LqL._AC_SL1000_.jpg",
                "price": 13,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["cute", "contemporary", "kid", "lights", "decor", "white" ]
            },
            {
                "name": "rolling cart pink",
                "sims_name": "popcart",
                "buy_url": "https://a.co/d/cWNaSxJ",
                "sims_pic_url": "https://imgur.com/LO1PrkZ",
                "real_pic_url": "https://m.media-amazon.com/images/I/5120jRW-2mL._AC_SL1000_.jpg",
                "price": 50,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["simple", "kids", "contemporary", "storage", "pink", "decor", "cute"]
            },
            {
                "name": "fur rug",
                "sims_name": "Super-Fuzz Fuzz rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/everly-quinn-nakita-machine-woven-area-rug-in-white-w008358234.html?piid=1224792402",
                "sims_pic_url": "https://imgur.com/iaJefXz",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/32169864/resize-h755-w755%5Ecompr-r85/2040/204061422/Nakitia+Machine+Woven+%2F+Power+Loomed+Performance+White+Machine+Washable+Rug.jpg",
                "price": 55,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["luxe", "glam", "contemporary", "chic", "rug", "decor", "white", "kid", "cite"]
            },
            {
                "name": "cloud shelf",
                "sims_name": "childhood wonder",
                "buy_url": "https://a.co/d/glqUZ92",
                "sims_pic_url": "https://imgur.com/mOSDQo7",
                "real_pic_url": "https://m.media-amazon.com/images/I/61ps48N3xTL._AC_SL1500_.jpg",
                "price": 17,
                "rooms": ["Unicorn Dreams"],
                "meta_tags": ["Kids", "Cute", "shelf", "storage", "pink", "purple"]
            },
            {
                "name": "school bus toybox",
                "sims_name": "Toys for tykes toybox",
                "buy_url": "https://a.co/d/47xpXJE",
                "sims_pic_url": "https://imgur.com/MHduNxc",
                "real_pic_url": "https://m.media-amazon.com/images/I/711ggnv8FxL._SL1357_.jpg",
                "price": 25,
                "rooms": ["Vroom Room"],
                "meta_tags": ["kids", "cute", "yellow", "toy", "storage"]
            },
            {
                "name": "blue rug",
                "sims_name": "Rug around",
                "buy_url": "https://a.co/d/4xnK9It",
                "sims_pic_url": "https://imgur.com/2W36O5V",
                "real_pic_url": "https://m.media-amazon.com/images/I/81r-KxDZGgL._AC_SL1440_.jpg",
                "price": 24,
                "rooms": ["Vroom Room"],
                "meta_tags": ["kid", "contemporary", "cute", "blue", "rug", "decor"]
            },
            {
                "name": "dragon",
                "sims_name": "Drago",
                "buy_url": "https://a.co/d/9yLVzcW",
                "sims_pic_url": "https://imgur.com/7NgwWJl",
                "real_pic_url": "https://m.media-amazon.com/images/I/71Q4uFBBjKL._AC_SX466_.jpg",
                "price": 90,
                "rooms": ["Vroom Room"],
                "meta_tags": ["kid", "cute", "toy", "green"]
            },
            {
                "name": "rolling cart blue",
                "sims_name": "popcart",
                "buy_url": "https://m.media-amazon.com/images/I/51SOGtHD2zL._AC_SL1000_.jpg",
                "sims_pic_url": "https://a.co/d/eBvm5KH",
                "real_pic_url": "https://imgur.com/b8D9rs9",
                "price": 30,
                "rooms": ["Vroom Room"],
                "meta_tags": ["simple", "kids", "contemporary", "storage", "blue", "decor", "cute"]
            },
            {
                "name": "racecar bed",
                "sims_name": "Racer dreams",
                "buy_url": "https://www.wayfair.com/baby-kids/pdp/zoomie-kids-aashish-twin-car-bed-w008768615.html?piid=1761765045",
                "sims_pic_url": "https://imgur.com/GUSp8XH",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/22270517/resize-h755-w755%5Ecompr-r85/3626/36268214/Aashish+Twin+Cars+Bed+by+Zoomie+Kids.jpg",
                "price": 277,
                "rooms": ["Vroom Room"],
                "meta_tags": ["Kid", "cute", "bed", "red", "toodler bed" ]
            },
            {
                "name": "panda chair",
                "sims_name": "best bear friend",
                "buy_url": "https://a.co/d/gdVehV8",
                "sims_pic_url": "https://imgur.com/d97UBUB",
                "real_pic_url": "https://m.media-amazon.com/images/I/616X1k2Ye0S._AC_SL1500_.jpg",
                "price": 70,
                "rooms": ["Vroom Room"],
                "meta_tags": ["Kid", "Cute", "black", "white", "chair" ]
            },
            {
                "name": "cat planter",
                "sims_name": "smitten kittens feline florals",
                "buy_url": "https://a.co/d/00D6cX2",
                "sims_pic_url": "https://i.imgur.com/uK7iIyG.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/41A25rgxZgL._AC_.jpg",
                "price": 8,
                "rooms": ["Zen Den"],
                "meta_tags": ["Cute", "plant", "pot", "multi", "white", "orage" ]
            },
            {
                "name": "lotus candle",
                "sims_name": "Blooming Lights",
                "buy_url": "https://a.co/d/8WBBavf",
                "sims_pic_url": "https://i.imgur.com/ZDVzExF.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/413hQe6UPQL._AC_.jpg",
                "price": 16,
                "rooms": ["Zen Den, quick bites, long talks"],
                "meta_tags": ["boho", "plant", "Eclectic", "BOHEMIAN", "decor", "blue", "purple", "candle"]
            },
            {
                "name": "arc lamp",
                "sims_name": "fringe of the elegance lamp",
                "buy_url": "https://a.co/d/4OOfS9w",
                "sims_pic_url": "https://i.imgur.com/PdNztKd.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71iwpsZVtaL._AC_SL1500_.jpg",
                "price": 130,
                "rooms": ["Zen Den"],
                "meta_tags": ["boho", "modern", "contemporary", "chic", "Eclectic", "BOHEMIAN", "lmap", "white", "gold", "black"]
            },
            {
                "name": "wicker basket",
                "sims_name": "basket of cozzies",
                "buy_url": "https://a.co/d/68WjRhK",
                "sims_pic_url": "https://i.imgur.com/AScesnX.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81yaZZfwYkL._AC_SL1500_.jpg",
                "price": 63,
                "rooms": ["Zen Den"],
                "meta_tags": ["classic", "rustic", "traditional", "Eclectic", "Shabby", "Chic", "brown", "wood", "stroage", "decor", "basket"]
            },
            {
                "name": "hanging planter",
                "sims_name": "green goddess pothos",
                "buy_url": "https://a.co/d/fIoBODf",
                "sims_pic_url": "https://i.imgur.com/gxMv0pX.png",
                "real_pic_url": "https://www.amazon.com/dp/B09VX72F64?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_3STM4DBZMZZGEJ4ZHF68",
                "price": 25,
                "rooms": ["Zen Den"],
                "meta_tags": ["plant", "Eclectic", "pot", "white", "decor", "boho", "bohiemian"]
            },
            {
                "name": "noodle candle",
                "sims_name": "the noddle candle",
                "buy_url": "https://www.etsy.com/listing/1173053554/wavy-sculptural-soy-wax-candle-home?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=squiggle+candles+blue&ref=sr_gallery-1-4&pro=1&sts=1&organic_search_click=1&variation0=2511071137",
                "sims_pic_url": "https://i.imgur.com/ogATGXc.png",
                "real_pic_url": "https://www.etsy.com/listing/1173053554/wavy-sculptural-soy-wax-candle-home?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=squiggle+candles+blue&ref=sr_gallery-1-4&pro=1&sts=1&organic_search_click=1&variation0=2511071137",
                "price": 17,
                "rooms": ["Zen Den"],
                "meta_tags": ["cute", "boho", "contemporary", "Eclectic", "BOHEMIAN", "blue", "multi", "candle"]
            },
            {
                "name": "moroccan rug",
                "sims_name": "Trouk fringe",
                "buy_url": "https://www.rugsusa.com/rugsusa/rugs/rugs-usa-moroccan-trellis/Gray/200RZBD16A-P.html",
                "sims_pic_url": "https://i.imgur.com/6aHMhet.png",
                "real_pic_url": "https://www.rug-images.com/products/osNew/roomImage/200RZBD16A.jpg?purpose=pdpLifestyleSmall",
                "price": 285,
                "rooms": ["Zen den"],
                "meta_tags": ["contemporary", "Modern", "Moroccan", "Shabby", "Chic", "cream", "grey", "rug", "decor"]
            },
            {
                "name": "blue sofa",
                "sims_name": "knock around couch",
                "buy_url": "https://www.wayfair.com/furniture/pdp/birch-lane-ophelie-87-rolled-arm-chesterfield-sofa-w005438470.html?piid=2124489610",
                "sims_pic_url": "https://i.imgur.com/iz9uoBW.png",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/46106533/resize-h755-w755%5Ecompr-r85/1789/178953001/Ophelie+87%27%27+Upholstered+Sofa.jpg",
                "price": 1,617,
                "rooms": ["Zen den"],
                "meta_tags": ["classic", "Eclectic", "Shabby", "Chic", "sofa", "coutch", "blue"]
            },
            {
                "name": "console table",
                "sims_name": "the crafty craftsman console table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/three-posts-schubert-console-table-w003641506.html",
                "sims_pic_url": "https://i.imgur.com/ksmJfsF.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/7324537/resize-h755-w755%5Ecompr-r85/1019/101974035/Schubert+50%27%27+Console+Table.jpg",
                "price": 320,
                "rooms": ["Zen den"],
                "meta_tags": ["classic",  "craftsman", "wood", "table", "side", "table", "console", "table"]
            },
            {
                "name": "industrial coffee table",
                "sims_name": "form and function industrial coffee table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/17-stories-howardwick-coffee-table-with-storage-w003560926.html",
                "sims_pic_url": "https://i.imgur.com/MTx1Cas.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/59924886/resize-h755-w755%5Ecompr-r85/1257/125745313/Howardwick+Coffee+Table.jpg",
                "price": 295,
                "rooms": ["Zen Den"],
                "meta_tags": ["Industrial", "Eclectic", "Shabby", "Chic", "table", "coffee", "table", "wood", "glass"]
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