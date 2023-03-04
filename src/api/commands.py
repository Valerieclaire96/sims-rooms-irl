
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
    # @app.cli.command("populate-fav_room-table")
    #     def generate_fav_room():


    @app.cli.command("populate-room-table")
    def generate_room_list():
        room_list = [
            {
                "name": "Dude, Where's my Closet?",
                "pic_url": "https://imgur.com/SmhGAwI",
            },
             {
                "name": "geeks4Sleep",
                "pic_url": "https://imgur.com/MT1HV5j",
            },
             {
                "name": "Lazy Susan’s Kitchen",
                "pic_url": "https://i.imgur.com/9WdnFoR.png",            },
             {
                "name": "Quick Bites, Long Talks",
                "pic_url": "https://i.imgur.com/tPG1Meg.png",
             },
             {
                "name": "The Fancy Man’s Study",
                "pic_url": "https://i.imgur.com/tPG1Meg.png",
             },
             {
                "name": "Straight As to Zzz",
                "pic_url": "https://i.imgur.com/YpAijUT.png",
            },
             {
                "name": "Tweenage Dirtbag",
                "pic_url": "https://imgur.com/HHILH8C",
            },
             {
                "name": "Unicorn Dreams",
                "pic_url": "https://imgur.com/iaJefXz",
            },
             {
                "name": "Vroom Room",
                "pic_url": "https://imgur.com/2W36O5V",
            },
             {
                "name": "Zen Den",
                "pic_url": "https://i.imgur.com/6aHMhet.png",
            },
        ]
        for room in room_list:
            new_room = Room(
                name = room['name'],
                pic_url = room['pic_url'],
                objects = room['objects'],
                meta_tags = room['meta_tags']
            )
            db.session.add(new_room)
            db.session.commit()

    @app.cli.command("populate-object-table")
    def generate_object_list():
        object_list = [
            {
                "name": "architecture art",
                "sims_name": "Roman Temple Architectural Study",
                "buy_url": "Architecture Art 4 : 18th C. English Townhouse Collection - Etsy",
                "sims_pic_url": "https://imgur.com/Lmr3ZMq",
                "real_pic_url": "https://i.etsystatic.com/8306577/r/il/b40bb7/3138741932/il_1140xN.3138741932_8jt9.jpg",
                "price": 58,
            },
            {
                "name": "lattice rug",
                "sims_name": "Lattice in Indoor-Outdoor Rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/alcott-hill-tylersburg-moroccan-trellis-ivorynavy-area-rug-alth6143.html?piid=25521865%2C38411307",
                "sims_pic_url": "https://imgur.com/SmhGAwI",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/84132909/resize-h1600-w1600%5Ecompr-r85/5860/58602179/Tylersburg+Machine+Woven+%2F+Power+Loomed+Performance+Rug.jpg",
                "price": 270,
            },
            {
                "name": "padded headboard",
                "sims_name": "The Princess and the Pineapple Bed",
                "buy_url": "https://a.co/d/6ghdt8J",
                "sims_pic_url": "https://imgur.com/JakzBPi",
                "real_pic_url": "https://m.media-amazon.com/images/I/71WpveLsHmL._AC_SL1500_.jpg",
                "price": 170,
            },
            {
                "name": "salt lamp",
                "sims_name": "Lamp Finds a Way",
                "buy_url": "https://a.co/d/daqgHzX",
                "sims_pic_url": "https://imgur.com/hiPfwrw",
                "real_pic_url": "https://m.media-amazon.com/images/I/612+MvvNgiL._AC_SL1500_.jpg",
                "price": 23,
            },
            {
                "name": "dog planter",
                "sims_name": "Puppulent Succulent",
                "buy_url": "https://a.co/d/1Lyzk8H",
                "sims_pic_url": "https://imgur.com/qmrGR5q",
                "real_pic_url": "https://m.media-amazon.com/images/I/61yj2yUTvFL._AC_SL1001_.jpg",
                "price": 22,
            },
            {
                "name": "clothing rack",
                "sims_name": "Backstreet Clothing Rack",
                "buy_url": "https://a.co/d/fWys2of",
                "sims_pic_url": "https://imgur.com/zPjohe7",
                "real_pic_url": "https://m.media-amazon.com/images/I/810YHmx21YL._AC_SL1500_.jpg",
                "price": 110,
            },
            {
                "name": "wicker hamper",
                "sims_name": "Wicker Whims Hamper",
                "buy_url": "https://a.co/d/epKkUWd",
                "sims_pic_url": "https://imgur.com/pxe6Lsa",
                "real_pic_url": "https://m.media-amazon.com/images/I/A1uwIeK-FfL._AC_SL1500_.jpg",
                "price": 115,
            },
            {
                "name": "industrial lamp",
                "sims_name": "Totality Rripod Floor Lamp",
                "buy_url": "https://a.co/d/fVWdzCz",
                "sims_pic_url": "https://imgur.com/aoWOTkb",
                "real_pic_url": "https://m.media-amazon.com/images/I/71QjFE+tq-L._AC_SL1500_.jpg",
                "price": 49,
            },
            {
                "name": "gaming chair",
                "sims_name": "Multitasker G",
                "buy_url": "https://a.co/d/0GeMmvK",
                "sims_pic_url": "https://imgur.com/UoIPr7e",
                "real_pic_url": "https://m.media-amazon.com/images/I/612r4sw1jYL._AC_SL1500_.jpg",
                "price": 180,
            },
            {
                "name": "gaming desk",
                "sims_name": "Pr-0 Gaming Desk",
                "buy_url": "https://a.co/d/6ihji1E",
                "sims_pic_url": "https://imgur.com/dAZrqCr",
                "real_pic_url": "https://m.media-amazon.com/images/I/612r4sw1jYL._AC_SL1500_.jpg",
                "price": 158,
            },
            {
                "name": "checkered rug",
                "sims_name": "Choose Your Aesthetic Rug",
                "buy_url": "https://a.co/d/gN23z9d",
                "sims_pic_url": "https://imgur.com/MT1HV5j",
                "real_pic_url": "https://m.media-amazon.com/images/I/91Lq6XCHLpL._AC_SL1500_.jpg",
                "price": 92,
            },
            {
                "name": "record art",
                "sims_name": "Free Association Collages",
                "buy_url": "https://a.co/d/bSoP5fq",
                "sims_pic_url": "https://imgur.com/O3kqb2S",
                "real_pic_url": "https://m.media-amazon.com/images/I/91OUnFry9bL._AC_SX466_.jpg",
                "price": 19,
            },
            {
                "name": "round table",
                "sims_name": "Sir Cumference Coffee Table",
                "buy_url": "https://a.co/d/89X9h0S",
                "sims_pic_url": "https://imgur.com/NWCjOxa",
                "real_pic_url": "https://m.media-amazon.com/images/I/717q7wg1ZhL._AC_SL1500_.jpg",
                "price": 34,
            },
            {
                "name": "wardrobe",
                "sims_name": "Night Before Dresser",
                "buy_url": "https://a.co/d/iCAD4AE",
                "sims_pic_url": "https://i.imgur.com/hcnNmZ1.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/51TXvzE-mCL._AC_.jpg",
                "price": 255,
            },
            {
                "name": "bamboo",
                "sims_name": "Palliatiude Potted bamboo",
                "buy_url": "https://a.co/d/ee6j2Y0",
                "sims_pic_url": "https://imgur.com/fWQxBXu",
                "real_pic_url": "https://m.media-amazon.com/images/I/81M46m8NvfL._AC_SL1500_.jpg",
                "price": 78,
            },
            {
                "name": "lava lamp",
                "sims_name": "The Green Lava Beacon",
                "buy_url": "https://a.co/d/8eIgrQu",
                "sims_pic_url": "https://imgur.com/NWCjOxa",
                "real_pic_url": "https://m.media-amazon.com/images/I/61dmJx+pZyL._AC_SL1500_.jpg",
                "price": 22,
            },
            {
                "name": "stripped planter",
                "sims_name": "Faustus the ZZ Plant",
                "buy_url": "https://a.co/d/hbOIGve",
                "sims_pic_url": "https://i.imgur.com/LNCop8r.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/612yDwcfJKL._AC_SL1500_.jpg",
                "price": 25,
            },
            {
                "name": "pet feeder",
                "sims_name": "Permate Programmatic Pet Feeder",
                "buy_url": "https://a.co/d/7ggdgBh",
                "sims_pic_url": "https://i.imgur.com/lb0PNzQ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/51N593Uu05L._AC_SL1500_.jpg",
                "price": 70,
            },
            {
                "name": "popcorn maker",
                "sims_name": "Sugar Corn Popcorn Popper",
                "buy_url": "https://a.co/d/0pRVdSz",
                "sims_pic_url": "https://i.imgur.com/BwIWcRY.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71eZwHSWsjL._AC_SL1500_.jpg",
                "price": 25,
            },
            {
                "name": "dutch oven",
                "sims_name": "The King's Cookware- by the Medlin Forge",
                "buy_url": "https://a.co/d/8tUe7mz",
                "sims_pic_url": "https://i.imgur.com/FLhNqne.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81MdPE8Q-4L._AC_SL1500_.jpg",
                "price": 50,
            },
            {
                "name": "barstool",
                "sims_name": "The Celestial",
                "buy_url": "https://a.co/d/13KAHNk",
                "sims_pic_url": "https://i.imgur.com/Fl4mF8E.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71PAf6HAJyS._AC_SL1500_.jpg",
                "price": 85,
            },
            {
                "name": "tea rack",
                "sims_name": "Simergy Tea Sensations",
                "buy_url": "https://a.co/d/81cVZXA",
                "sims_pic_url": "https://i.imgur.com/mGmroRT.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71NzBFARuQL._AC_SL1500_.jpg",
                "price": 23,
            },
            {
                "name": "knife rack",
                "sims_name": "Positronic Pro Magnetic Knife Rack",
                "buy_url": "https://a.co/d/giDUhto",
                "sims_pic_url": "https://i.imgur.com/6FDZkiQ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/41ztJBWqD-L._AC_.jpg",
                "price": 23,
            },
            {
                "name": "mc dining table",
                "sims_name": "All of the Things Table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/wade-logan-agla-hallway-console-table-w000364723.html",
                "sims_pic_url": "https://i.imgur.com/RxOkVfY.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/93954241/resize-h755-w755%5Ecompr-r85/3492/34928790/Agla+40%27%27+Solid+Wood+Console+Table.jpg",
                "price": 350,
            },
            {
                "name": "mc console table",
                "sims_name": "Moder Mid-Century Marvel",
                "buy_url": "https://www.wayfair.com/furniture/pdp/birch-lane-geoff-glass-dining-table-w008599694.html",
                "sims_pic_url": "https://i.imgur.com/EeNoQ2R.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/38840974/resize-h1600-w1600%5Ecompr-r85/2326/232656119/Geoff+43.3%27%27+Dining+Table.jpg",
                "price": 250,
            },
            {
                "name": "floor lamp",
                "sims_name": "Not All Included' Lamp without Storage",
                "buy_url": "https://a.co/d/0jjtRvy",
                "sims_pic_url": "https://i.imgur.com/dZea7Oz.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81wgW-40KxL._AC_SL1500_.jpg",
                "price": 170,
            },
            {
                "name": "mc dining chair",
                "sims_name": "The Trendsitter",
                "buy_url": "https://a.co/d/5XnHCDE",
                "sims_pic_url": "https://i.imgur.com/E361OMJ.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71zYPalXIwL._AC_SL1500_.jpg",
                "price": 300,
            },
            {
                "name": "studded arm chair",
                "sims_name": "Executive Guest Chair",
                "buy_url": "https://a.co/d/8cEOsm4",
                "sims_pic_url": "https://imgur.com/RWKMMIc",
                "real_pic_url": "https://m.media-amazon.com/images/I/71NK46jk6lL._AC_SL1500_.jpg",
                "price": 180,
            },
            {
                "name": "globe bar",
                "sims_name": "16th Century Monte Vista Globe Bar ",
                "buy_url": "https://a.co/d/9CFZr8n",
                "sims_pic_url": "https://imgur.com/uML6YY1",
                "real_pic_url": "https://m.media-amazon.com/images/I/A1+Zq-qJoDL._AC_SL1500_.jpg",
                "price": 170,
            },
            {
                "name": "bankers lamp",
                "sims_name": "The Artisan",
                "buy_url": "https://a.co/d/a2gD9WC",
                "sims_pic_url": "https://imgur.com/rtiTdQq",
                "real_pic_url": "https://m.media-amazon.com/images/I/71-8Kce+v2S._AC_SX679_.jpg",
                "price": 50,
            },
            {
                "name": "persian rug",
                "sims_name": "Threads of Fortune Rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/langley-street-edens-oriental-burgundy-area-rug-w004775928.html?piid=1606445080",
                "sims_pic_url": "https://imgur.com/jG5GOPd",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/07880182/resize-h755-w755%5Ecompr-r85/9762/97620517/Edens+Machine+Woven+%2F+Power+Loomed+Performance+Burgundy+Rug.jpg",
                "price": 180,
            },
            {
                "name": "executive desk chair",
                "sims_name": "Executron Executive Desk Throne",
                "buy_url": "https://www.wayfair.com/furniture/pdp/lark-manor-murphie-high-back-traditional-tufted-leathersoft-executive-swivel-ergonomic-office-chair-w001944761.html?piid%5B0%5D=933975933",
                "sims_pic_url": "https://imgur.com/JPUugQj",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/10739145/resize-h755-w755%5Ecompr-r85/1933/193366503/Murphie+High+Back+Traditional+Tufted+LeatherSoft+Executive+Swivel+Ergonomic+Office+Chair.jpg",
                "price": 520,
            },
            {
                "name": "executive desk",
                "sims_name": "Very Impressive Lawyer-y Desk",
                "buy_url": "Hekman 72'' Desk | Wayfair",
                "sims_pic_url": "https://imgur.com/fdf1RFJ",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/15056160/resize-h755-w755%5Ecompr-r85/1047/104759591/72%27%27+Desk.jpg",
                "price": 3998,
            },
            {
                "name": "leaf art",
                "sims_name": "Simple and Clean Art",
                "buy_url": "https://a.co/d/8tjebEh",
                "sims_pic_url": "https://i.imgur.com/493s267.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81ZlycohRdL._AC_SL1500_.jpg",
                "price": 30,
            },
            {
                "name": "mirror with lights",
                "sims_name": "Fit Full Length Vanity Mirror",
                "buy_url": "https://a.co/d/16aFJCB",
                "sims_pic_url": "https://i.imgur.com/43Tnda1.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71Ht6+RY-qL._AC_SL1200_.jpg",
                "price": 106,
            },
            {
                "name": "directors chair",
                "sims_name": "Just a Finch Directors Chair",
                "buy_url": "https://a.co/d/8tRdkuW",
                "sims_pic_url": "https://i.imgur.com/reKadqx.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/91I9mjcPpeL._AC_SL1500_.jpg",
                "price": 93,
            },
            {
                "name": "white gold dresser",
                "sims_name": "Perplexed Dresser",
                "buy_url": "https://a.co/d/e0zYoV6",
                "sims_pic_url": "https://i.imgur.com/YywYqrv.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71TRhy+wLlL._AC_SL1500_.jpg",
                "price": 220,
            },
            {
                "name": "pink floyd poster",
                "sims_name": "Hey I Like That Poster Too",
                "buy_url": "https://a.co/d/3etkW4s",
                "sims_pic_url": "https://imgur.com/DWyyeQM",
                "real_pic_url": "https://m.media-amazon.com/images/I/31By9mlOVLL._AC_.jpg",
                "price": 12,
            },
            {
                "name": "naruto rug",
                "sims_name": "Reliable Rug",
                "buy_url": "https://a.co/d/aZW7zSv",
                "sims_pic_url": "https://imgur.com/HHILH8C",
                "real_pic_url": "https://m.media-amazon.com/images/I/61MXoRUAi-L._AC_SL1500_.jpg",
                "price": 33,
            },
            {
                "name": "desk lamp",
                "sims_name": "Lex Light by Desk Pix",
                "buy_url": "https://a.co/d/0xvIyyU",
                "sims_pic_url": "https://imgur.com/YPVZA0l",
                "real_pic_url": "https://m.media-amazon.com/images/I/61R7hBIB0jL._AC_SL1500_.jpg",
                "price": 50,
            },
            {
                "name": "rice paper lamp",
                "sims_name": "You've Got The Light",
                "buy_url": "https://a.co/d/dfaU8Nv",
                "sims_pic_url": "https://imgur.com/6wtNhm3",
                "real_pic_url": "https://m.media-amazon.com/images/I/71nP6CvGTAL._AC_SL1500_.jpg",
                "price": 60,
            },
            {
                "name": "bean bag",
                "sims_name": "Chair of Many Colors",
                "buy_url": "https://a.co/d/0M83Iwa",
                "sims_pic_url": "https://imgur.com/i0yK226",
                "real_pic_url": "https://m.media-amazon.com/images/I/41OYjcpRr4L._AC_.jpg",
                "price": 17,
            },
            {
                "name": "bunk bed",
                "sims_name": "Metal Frame Top Bunk",
                "buy_url": "https://a.co/d/8hZDNyl",
                "sims_pic_url": "https://imgur.com/VygFyk8",
                "real_pic_url": "https://m.media-amazon.com/images/I/71e8EANp6ML._AC_SL1500_.jpg",
                "price": 210,
            },
            {
                "name": "wall decal",
                "sims_name": "Floating Away",
                "buy_url": "https://a.co/d/fMJOxL9",
                "sims_pic_url": "https://imgur.com/x87KkeL",
                "real_pic_url": "https://m.media-amazon.com/images/I/71HBJNvLPwS._AC_SL1300_.jpg",
                "price": 12,
            },
            {
                "name": "teddy bear",
                "sims_name": "The Lots of Love Bear",
                "buy_url": "https://a.co/d/dfSs6jS",
                "sims_pic_url": "https://imgur.com/3TMfnyS",
                "real_pic_url": "https://m.media-amazon.com/images/I/51FSfBMPzXL._AC_SL1000_.jpg",
                "price": 15,
            },
            {
                "name": "unicorn",
                "sims_name": "Uni",
                "buy_url": "https://a.co/d/b181DG1",
                "sims_pic_url": "https://imgur.com/LNPgEbX",
                "real_pic_url": "https://m.media-amazon.com/images/I/71f0m-0-t5L._AC_SX425_.jpg",
                "price": 70,
            },
            {
                "name": "butterfly chair",
                "sims_name": "The Gordian Spritz",
                "buy_url": "https://a.co/d/2uTy8cP",
                "sims_pic_url": "https://imgur.com/C3DySEs",
                "real_pic_url": "https://m.media-amazon.com/images/I/710NuDZK2FL._AC_SL1500_.jpg",
                "price": 20,
            },
            {
                "name": "house toddler bed",
                "sims_name": "The Freezepop Sleep Spot",
                "buy_url": "https://a.co/d/h4Iz4c2",
                "sims_pic_url": "https://imgur.com/ePPYIWK",
                "real_pic_url": "https://m.media-amazon.com/images/I/71fQae7TEjL._AC_SL1500_.jpg",
                "price": 310,
            },
            {
                "name": "string lights",
                "sims_name": "Say Good Night Little Lights",
                "buy_url": "https://a.co/d/5HQuT26",
                "sims_pic_url": "https://imgur.com/OwbrUao",
                "real_pic_url": "https://m.media-amazon.com/images/I/61kNKty4LqL._AC_SL1000_.jpg",
                "price": 13,
            },
            {
                "name": "rolling cart pink",
                "sims_name": "Popcart",
                "buy_url": "https://a.co/d/cWNaSxJ",
                "sims_pic_url": "https://imgur.com/LO1PrkZ",
                "real_pic_url": "https://m.media-amazon.com/images/I/5120jRW-2mL._AC_SL1000_.jpg",
                "price": 50,
            },
            {
                "name": "fur rug",
                "sims_name": "Super-Fuzz Fuzz Rug",
                "buy_url": "https://www.wayfair.com/rugs/pdp/everly-quinn-nakita-machine-woven-area-rug-in-white-w008358234.html?piid=1224792402",
                "sims_pic_url": "https://imgur.com/iaJefXz",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/32169864/resize-h755-w755%5Ecompr-r85/2040/204061422/Nakitia+Machine+Woven+%2F+Power+Loomed+Performance+White+Machine+Washable+Rug.jpg",
                "price": 55,
            },
            {
                "name": "cloud shelf",
                "sims_name": "Childhood Wonder",
                "buy_url": "https://a.co/d/glqUZ92",
                "sims_pic_url": "https://imgur.com/mOSDQo7",
                "real_pic_url": "https://m.media-amazon.com/images/I/61ps48N3xTL._AC_SL1500_.jpg",
                "price": 17,
            },
            {
                "name": "school bus toybox",
                "sims_name": "Toys for Tykes Toybox",
                "buy_url": "https://a.co/d/47xpXJE",
                "sims_pic_url": "https://imgur.com/MHduNxc",
                "real_pic_url": "https://m.media-amazon.com/images/I/711ggnv8FxL._SL1357_.jpg",
                "price": 25,
            },
            {
                "name": "blue rug",
                "sims_name": "Rug Around",
                "buy_url": "https://a.co/d/4xnK9It",
                "sims_pic_url": "https://imgur.com/2W36O5V",
                "real_pic_url": "https://m.media-amazon.com/images/I/81r-KxDZGgL._AC_SL1440_.jpg",
                "price": 24,
            },
            {
                "name": "dragon",
                "sims_name": "Drago",
                "buy_url": "https://a.co/d/9yLVzcW",
                "sims_pic_url": "https://imgur.com/7NgwWJl",
                "real_pic_url": "https://m.media-amazon.com/images/I/71Q4uFBBjKL._AC_SX466_.jpg",
                "price": 90,
            },
            {
                "name": "rolling cart blue",
                "sims_name": "Popcart",
                "buy_url": "https://m.media-amazon.com/images/I/51SOGtHD2zL._AC_SL1000_.jpg",
                "sims_pic_url": "https://a.co/d/eBvm5KH",
                "real_pic_url": "https://imgur.com/b8D9rs9",
                "price": 30,
            },
            {
                "name": "racecar bed",
                "sims_name": "Racer Dreams",
                "buy_url": "https://www.wayfair.com/baby-kids/pdp/zoomie-kids-aashish-twin-car-bed-w008768615.html?piid=1761765045",
                "sims_pic_url": "https://imgur.com/GUSp8XH",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/22270517/resize-h755-w755%5Ecompr-r85/3626/36268214/Aashish+Twin+Cars+Bed+by+Zoomie+Kids.jpg",
                "price": 277,
            },
            {
                "name": "panda chair",
                "sims_name": "Best Bear Friend",
                "buy_url": "https://a.co/d/gdVehV8",
                "sims_pic_url": "https://imgur.com/d97UBUB",
                "real_pic_url": "https://m.media-amazon.com/images/I/616X1k2Ye0S._AC_SL1500_.jpg",
                "price": 70,
            },
            {
                "name": "cat planter",
                "sims_name": "Smitten Kittens Feline Florals",
                "buy_url": "https://a.co/d/00D6cX2",
                "sims_pic_url": "https://i.imgur.com/uK7iIyG.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/41A25rgxZgL._AC_.jpg",
                "price": 8,
            },
            {
                "name": "lotus candle",
                "sims_name": "Blooming Lights",
                "buy_url": "https://a.co/d/8WBBavf",
                "sims_pic_url": "https://i.imgur.com/ZDVzExF.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/413hQe6UPQL._AC_.jpg",
                "price": 16,
            },
            {
                "name": "arc lamp",
                "sims_name": "Fringe of the Elegance Lamp",
                "buy_url": "https://a.co/d/4OOfS9w",
                "sims_pic_url": "https://i.imgur.com/PdNztKd.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/71iwpsZVtaL._AC_SL1500_.jpg",
                "price": 130,
            },
            {
                "name": "wicker basket",
                "sims_name": "basket of cozzies",
                "buy_url": "https://a.co/d/68WjRhK",
                "sims_pic_url": "https://i.imgur.com/AScesnX.png",
                "real_pic_url": "https://m.media-amazon.com/images/I/81yaZZfwYkL._AC_SL1500_.jpg",
                "price": 63,
            },
            {
                "name": "hanging planter",
                "sims_name": "Green Goddess Pothos",
                "buy_url": "https://a.co/d/fIoBODf",
                "sims_pic_url": "https://i.imgur.com/gxMv0pX.png",
                "real_pic_url": "https://www.amazon.com/dp/B09VX72F64?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_3STM4DBZMZZGEJ4ZHF68",
                "price": 25,
            },
            {
                "name": "noodle candle",
                "sims_name": "The Noddle Candle",
                "buy_url": "https://www.etsy.com/listing/1173053554/wavy-sculptural-soy-wax-candle-home?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=squiggle+candles+blue&ref=sr_gallery-1-4&pro=1&sts=1&organic_search_click=1&variation0=2511071137",
                "sims_pic_url": "https://i.imgur.com/ogATGXc.png",
                "real_pic_url": "https://www.etsy.com/listing/1173053554/wavy-sculptural-soy-wax-candle-home?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=squiggle+candles+blue&ref=sr_gallery-1-4&pro=1&sts=1&organic_search_click=1&variation0=2511071137",
                "price": 17,
            },
            {
                "name": "moroccan rug",
                "sims_name": "Trouk Fringe",
                "buy_url": "https://www.rugsusa.com/rugsusa/rugs/rugs-usa-moroccan-trellis/Gray/200RZBD16A-P.html",
                "sims_pic_url": "https://i.imgur.com/6aHMhet.png",
                "real_pic_url": "https://www.rug-images.com/products/osNew/roomImage/200RZBD16A.jpg?purpose=pdpLifestyleSmall",
                "price": 285,
            },
            {
                "name": "blue sofa",
                "sims_name": "Knock Around Couch",
                "buy_url": "https://www.wayfair.com/furniture/pdp/birch-lane-ophelie-87-rolled-arm-chesterfield-sofa-w005438470.html?piid=2124489610",
                "sims_pic_url": "https://i.imgur.com/iz9uoBW.png",
                "real_pic_url": "https://secure.img1-fg.wfcdn.com/im/46106533/resize-h755-w755%5Ecompr-r85/1789/178953001/Ophelie+87%27%27+Upholstered+Sofa.jpg",
                "price": 1617,
            },
            {
                "name": "console table",
                "sims_name": "The Crafty Craftsman Console Table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/three-posts-schubert-console-table-w003641506.html",
                "sims_pic_url": "https://i.imgur.com/ksmJfsF.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/7324537/resize-h755-w755%5Ecompr-r85/1019/101974035/Schubert+50%27%27+Console+Table.jpg",
                "price": 320,
            },
            {
                "name": "industrial coffee table",
                "sims_name": "Form and Function Industrial Coffee Table",
                "buy_url": "https://www.wayfair.com/furniture/pdp/17-stories-howardwick-coffee-table-with-storage-w003560926.html",
                "sims_pic_url": "https://i.imgur.com/MTx1Cas.png",
                "real_pic_url": "https://secure.img1-cg.wfcdn.com/im/59924886/resize-h755-w755%5Ecompr-r85/1257/125745313/Howardwick+Coffee+Table.jpg",
                "price": 295,
            },
        ]
        for r_object in object_list:
            new_object = Object(
                name = r_object['name'],
                sims_name = r_object['sims_name'],
                buy_url = r_object['buy_url'],
                sims_pic_url = r_object['sims_pic_url'],
                real_pic_url = r_object['real_pic_url'],
                price = r_object['price'],
                rooms = r_object['rooms'],
                meta_tags = r_object['meta_tags']
            )
            db.session.add(new_object)
            db.session.commit()

    @app.cli.command("populate-object_room-table")
    def generate_object_room_list():
        room_object_list = [
            {
                "rooms": ["Zen Den"],
                "objects": ["cat planter","lotus candle","arc lamp","wicker basket","handing planter","noddle candle","moroccan rug","blue sofa","console table","industrial coffee table"],
            },
            {
                "rooms": ["Vroom Room"],
                "objects": ["school bus toybox","blue rug","dragon","rolling cart","racecar bed","panda chair"]
            },
            {
                "rooms": ["Unicorn Dreams"],
                "objects": ["wall decal","teddy bear","unicorn","butterfly chair","house toddler bed","string lights","rolling car pink"]
            },
            {
                "rooms": ["Tweenage Dirtbag"],
                "objects": ["pink floyd poster","nautro rug","desk lamp","rice paper lamp","bean bag","bunk bed"]
            },
            {
                "rooms": ["Straight As to Zzz"],
                "objects": ["leaf art", "mirror with lights", "director’s chair", "white gold dresser", "salt lamp"]
            },
            {
                "rooms": ["The Fancy Man's Study"],
                "objects":  ["studded arm chair", "globe bar", "bankers lamp", "Persian rug", "executive desk chair", "executive desk"]
            },
            {
                "rooms": ["Quick Bites, Long Talks"],
                "objects": ["mc dining table", "mc console table", "floor lamp", "md dining chair", "architecture art", "lotus candle"]
            },
            {
                "rooms": ["Lazy Susan's Kitchen"],
                "objects":  ["stripped planter" ,"pet feeder", "popcorn maker", "dutch oven", "barstool", "tea rack", "knife rack"]
            },
            {
                "rooms": ["sleep4geeks"],
                "objects":  ["indstrial lamp", "gaming chair", "gaming desk", "checkered rug", "record art", "round table", "wardrobe","bamboo","lava lamp"]
            },
            {
                "rooms": ["Dude, Where's my Closet?"],
                "objects": ["architecture art" , "lattice rug", "padded headboard", "salt lamp", "dog planter", "clothing rack", "wicker hamper"]
            }
        ]
        for r_o in room_object_list:
            new_r_o = room_object(
                room = room["name"],
                object = object["name"]
            )
            db.session.add(new_r_o)
            db.session.commit()

    @app.cli.command("populate-meta_room-table")
    def generate_meta_room_list():
        meta_room_list = [
            {
                "room": ["Dude, Where's my Closet?"],
                "meta_tags": ["contemporary", "modern", "minimalist", "simple", "bedroom"]
            },
            {
                "room": ["sleep4geeks"],
                "meta_tags": ["teen", "contemporary", "bedroom", "black"]
            },
            {
                "room": ["Lazy Susan's Kitchen"],
                "meta_tags": ["modern" , "contemporary", "retro", "kitchen", "atomic", "mid century"]
            },
            {
                "room": ["Quick Bites, Long Talks"],
                "meta_tags": ["mid century modern", "modern", "contemporary","dining room", "vintage", "scandinavian"]
            },
            {
                "room": ["The Fancy Man's Study"],
                "meta_tags":  ["office", "study", "classic", "traditional" , "brown","wood"]
            },
            {
                "room": ["Straight As to Zzz"],
                "meta_tags":  ["teen", "contemporary","modern","chic","luxe","glamor","bedroom"]

            },
            {
                "rooms": ["Tweenage Dirtbag"],
                "meta_tags": ["kid","teen","contemporary", "bedroom","white","blue"]
            },
            {
                "room": ["Unicorn Dreams"],
                "meta_tags": ["kids","cute","pink","purple"]
            },
            {
                "room": ["Vroom Room"],
                "meta_tags": ["kids","cute","blue"]
            },
            {
                "rooms": ["Zen Den"],
                "meta_tags": ["boho", "eclectic", "bohemian", "shabby chic", "living room"] 
            }
        ]
        for room in meta_room_list:
            new_room = meta_room(
                room = room["name"],
                meta_tags = meta["tag"]
            )
            db.session.add(new_room)
            db.session.commit()
    
    @app.cli.command("populate-meta_object-table")
    def generate_meta_object_list():
        meta_object_list = [
            {
                "name": "architecture art",
                "meta_tags": ["classic", "traditional", "farmhouse", "black", "white", "decor", "picture"],
            },
            {
                "name": "lattice rug",
                "meta_tags": ["simple", "contemporary", "brown", "white", "rug", "decor"]
            },
            {           
                "name": "padded headboard",
                "meta_tags": ["modern", "simple", "minimalist"]
            },
            {
                "name": "salt lamp",
                "meta_tags": ["boho", "rustic", "eclectic", "orange", "wood", "lamp", "decor"]
            },
            {
                "name": "dog planter",
                "meta_tags": ["cute", "plant", "eclectic", "plant", "pot", "black", "white", "brown", "green", "multicolor"]
            },
            {
                "name": "clothing rack",
                "meta_tags": ["contemporary", "minimalist", "chic", "black", "wood", "dresser", "clothing", "rack"]
            },
            {
                "name": "wicker hamper",
                "meta_tags": ["farmhouse", "rustic", "wood", "brown", "hamper", "laundry", "basket"]
            },
            {
                "name": "industrial lamp",
                "meta_tags": ["industrial", "dclectic", "black", "silver", "lamp", "teen"]
            },
            {
                "name": "gaming chair",
                "meta_tags": ["teen", "contemporary", "teen", "chair", "desk chair", "gaming chair", "black", "purple", "gaming"]
            },
            {
                "name": "gaming desk",
                "meta_tags": ["teen", "contemporary", "teen", "black", "multcolor", "rainbow", "desk", "gaming"]
            },
            {
                "name": "checkered rug",
                "meta_tags": ["teen", "contemporary", "rug", "checkered", "black", "white"]
            },
            {
                "name": "record art",
                "meta_tags": ["boho", "teen", "decor", "art", "rainbow", "multi", "black", "vintage"]
            },
            {
                "name": "round table",
                "meta_tags": ["modern", "teen", "minimalist", "chic", "table", "coffee table", "side table", "night stand", "contemporary", "black", "circle"]
            },
            {
                "name": "wardrobe",
                "meta_tags": ["teen", "contemporary", "storage", "dresser", "wardrobe", "wood", "brown", "expresso"]
            },
            {
                "name": "bamboo",
                "meta_tags": ["modern", "chic", "boho", "contemporary", "teen", "green", "black", "plant" ]
            },
            {
                "name": "lava lamp",
                "meta_tags": ["retro", "vintage", "green", "atomic", "lamp", "decor"]
            },
            {
                "name": "stripped planter",
                "meta_tags": ["modern" "glam", "luxe", "minimalist", "grey", "white", "gold", "planter"]
            },
            {
                "name": "pet feeder",
                "meta_tags": ["pets", "black", "tech", "pet", "feeder", "modern", "minimalist" ]
            },
            {
                "name": "popcorn maker",
                "meta_tags": ["tech", "applicance", "red" ]
            },
            {
                "name": "dutch oven",
                "meta_tags": ["classic", "farmhouse", "rustic", "red", "cookware"]
            },
            {
                "name": "barstool",
                "meta_tags": ["mid century modern", "atomic", "chic", "mordern", "red", "stool", "bar stool", "swivle"]
            },
            {
                "name": "tea rack",
                "meta_tags": ["contemporary", "decor", "storage", "wood", "black"]
            },
            {
                "name": "knife rack",
                "meta_tags": ["modern", "industrial", "contemporary", "silver", "decor", "storage"]
            },
            {
                "name": "mc dining table",
                "meta_tags": ["mid", "century", "modern", "modern", "contemporary", "scandinavian", "table", "dining table", "wood", "glass"]
            },
            {
                "name": "mc console table",
                "meta_tags": ["mid", "century", "modern", "modern", "contemporary", "scandinavian"]
            },
            {
                "name": "floor lamp",
                "meta_tags": ["mid century modern", "modern", "scandinavian", "wood", "black", "lamp", "decor"]
            },
            {
                "name": "mc dining chair",
                "meta_tags": ["mid", "century", "modern", "chair", "dining chair", "wood", "retro"]
            },
            {
                "name": "studded arm chair",
                "meta_tags": ["classic", "traditional", "black", "gold", "chair", "arm chair"]
            },
            {
                "name": "globe bar",
                "meta_tags": ["classic", "traditional",  "brown", "gold", "black", "bar"]
            },
            {
                "name": "bankers lamp",
                "meta_tags": ["classic", "traditional", "gold", "green", "lamp"]
            },
            {
                "name": "persian rug",
                "meta_tags": ["classic", "persian", "red", "blue", "multi", "rug", "decor"]
            },
            {
                "name": "executive desk chair",
                "meta_tags": ["classic", "traditional", "black", "gold", "chair", "desk chair" ]
            },
            {
                "name": "executive desk",
                "meta_tags": ["classic", "traditional", "wood", "brown", "desk"]
            },
            {
                "name": "leaf art",
                "meta_tags": ["teen", "contemporary", "art", "decor", "white", "green", "picture"]
            },
            {
                "name": "mirror with lights",
                "meta_tags": ["teen", "contemporary", "white", "glam", "mirror", "lighting"]
            },
            {
                "name": "directors chair",
                "meta_tags": ["teen", "contemporary", "eclectic", "chair", "white"]
            },
            {
                "name": "white gold dresser",
                "meta_tags": ["teen", "modern", "chic", "white", "gold", "glam", "dresser", "storage"]
            },
            {
                "name": "pink floyd poster",
                "meta_tags": ["retro", "vintage", "black", "multi", "rainbow", "poster", "decor", "kid", "teen"]
            },
            {
                "name": "naruto rug",
                "meta_tags": ["kid", "teen", "black", "red", "decor", "rug", "teen", "kid"]
            },
            {
                "name": "desk lamp",
                "meta_tags": ["contemporary", "blue", "wood", "lamp"]
            },
            {
                "name": "rice paper lamp",
                "meta_tags": ["contemporary", "modern", "black", "white", "lamp", "teen", "kid"]
            },
            {
                "name": "bean bag",
                "meta_tags": ["kid", "teen", "black", "chair" ]
            },
            {
                "name": "bunk bed",
                "meta_tags": ["Kid", "teen", "black", "bed" ]
            },
            {
                "name": "wall decal",
                "meta_tags": ["kid" "cute" "decal" "decor" "multi" "pink" "purple"]
            },
            {
                "name": "teddy bear",
                "meta_tags": ["kid", "cute", "pink", "red", "toy" ]
            },
            {
                "name": "unicorn",
                "meta_tags": ["kid", "cute", "pink", "purple", "toy"]
            },
            {
                "name": "butterfly chair",
                "meta_tags": ["kid", "cute", "pink", "blue", "chair"]
            },
            {
                "name": "house toddler bed",
                "meta_tags": ["kid", "cute", "white", "bed", "toddler bed"]
            },
            {
                "name": "string lights",
                "meta_tags": ["cute", "contemporary", "kid", "lights", "decor", "white" ]
            },
            {
                "name": "rolling cart pink",
                "meta_tags": ["simple", "kids", "contemporary", "storage", "pink", "decor", "cute"]
            },
            {
                "name": "fur rug",
                "meta_tags": ["luxe", "glam", "contemporary", "chic", "rug", "decor", "white", "kid", "cite"]
            },
            {
                "name": "cloud shelf",
                "meta_tags": ["Kids", "cute", "shelf", "storage", "pink", "purple"]
            },
            {
                "name": "school bus toybox",
                "meta_tags": ["kids", "cute", "yellow", "toy", "storage"]
            },
            {
                "name": "blue rug",
                "meta_tags": ["kid", "contemporary", "cute", "blue", "rug", "decor"]
            },
            {
                "name": "dragon",
                "meta_tags": ["kid", "cute", "toy", "green"]
            },
            {
                "name": "rolling cart blue",
                "meta_tags": ["simple", "kids", "contemporary", "storage", "blue", "decor", "cute"]
            },
            {
                "name": "racecar bed",
                "meta_tags": ["kid", "cute", "bed", "red", "toodler bed" ]
            },
            {
                "name": "panda chair",
                "meta_tags": ["kid", "cute", "black", "white", "chair" ]
            },
            {
                "name": "cat planter",
                "meta_tags": ["cute", "plant", "pot", "multi", "white", "orage" ]
            },
            {
                "name": "lotus candle",
                "meta_tags": ["boho", "plant", "eclectic", "bohemian", "decor", "blue", "purple", "candle"]
            },
            {
                "name": "arc lamp",
                "meta_tags": ["boho", "modern", "contemporary", "chic", "eclectic", "bohemian", "lamp", "white", "gold", "black"]
            },
            {
                "name": "wicker basket",
                "meta_tags": ["classic", "rustic", "traditional", "eclectic", "shabby", "chic", "brown", "wood", "storage", "decor", "basket"]
            },
            {
                "name": "hanging planter",
                "meta_tags": ["plant", "eclectic", "pot", "white", "decor", "boho", "bohiemian"]
            },
            {
                "name": "noodle candle",
                "meta_tags": ["cute", "boho", "contemporary", "eclectic", "bohemian", "blue", "multi", "candle"]
            },
            {
                "name": "moroccan rug",
                "meta_tags": ["contemporary", "modern", "moroccan", "Ssabby", "chic", "cream", "grey", "rug", "decor"]
            },
            {
                "name": "blue sofa",
                "meta_tags": ["classic", "eclectic", "shabby", "chic", "sofa", "coutch", "blue"]
            },
            {
                "name": "console table",
                "meta_tags": ["classic",  "craftsman", "wood", "table", "side", "table", "console", "table"]
            },
            {
                "name": "industrial coffee table",
                "meta_tags": ["industrial", "eclectic", "shabby", "chic", "table", "coffee", "table", "wood", "glass"]
            },

        ]

    @app.cli.command("populate-meta-table")
    def generate_meta_list():
        meta_list = [
            {
                "tag" : "kids"
            },
            {
                "tag" : "wood"
            },
            {
                "tag" : "kitchen"
            },
        ]
        for description in meta_list:
            new_tag = Meta(
                tag = description['tag']
            )
            db.session.add(new_tag)
            db.session.commit()