
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
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "mirror with lights",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "directors chair",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "white gold dresser",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "pink floyd poster",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "naruto rug",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "desk lamp",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "rice paper lamp",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "bean bag",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "bunk bed",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "wall decal",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "teddy bear",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "unicorn",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "butterfly chair",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "house toddler bed",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "string lights",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "rolling cart pink",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "fur rug",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "cloud shelf",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "school bus toybox",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "blue rug",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "dragon",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "rolling cart blue",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "racecar bed",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "panda chair",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "cat planter",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "lotus candle",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "arc lamp",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "wicker basket",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "hanging planter",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "noodle candle",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "moroccan rug",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "blue rug",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "console table",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
            },
            {
                "name": "industrial coffee table",
                "sims_name": "",
                "buy_url": "",
                "sims_pic_url": "",
                "real_pic_url": "",
                "price": ,
                "rooms": [""],
                "meta_tags": []
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