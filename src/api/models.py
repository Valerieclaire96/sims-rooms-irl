from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# many to many relationship between user and rooms- used for identitifying favorited rooms
# at the top because the user table calls on this is as secondary in its relationship with rooms
fav_room = db.Table('fav_room',
            db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True),
            db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
            )
# many to many relationship between user and objects- used for identitifying favorited objects
# at the top because the user table calls on this is as secondary in its relationship with objects
fav_object = db.Table('fav_object',
            db.Column("object_id", db.Integer, db.ForeignKey("object.id"), primary_key=True),
            db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
            )

# user table with relationships to rooms and objects
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    profile_pic = db.Column(db.String(120), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # name to describe the relationship, then the name of the other table
    # the secondary is the table that defines the many to many relationship between the two tables
    # the back populations refers to the relationship to user created in the room table 
    user_rooms = db.relationship("Room",
                                secondary=fav_room,
                                back_populates="faved_rooms",
                                )
    #same as above but for objects
    user_objects = db.relationship("Object",
                                secondary=fav_object,
                                back_populates="faved_objects",
                                )
    # This is how the artist will print in the console, just the name
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_room": [room.serialize() for room in self.user_rooms],
            "user_objects": [r_object.serialize() for r_object in self.user_objects],
            # do not serialize the password, its a security breach
        }



# describes the many to many relationship between rooms and objects
room_object = db.Table('room_object',
            db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True),
            db.Column("object_id", db.Integer, db.ForeignKey("object.id"), primary_key=True),
            )

# describes the many to many relationship between rooms and meta
# the meta table is used to keep track of idenfifying characters that can apply to multiple rooms and objects
meta_room = db.Table('meta_room',
            db.Column("meta_id", db.Integer, db.ForeignKey("meta.id"), primary_key=False),
            db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True),
            )
# describes the many to many relationship between objects and meta
meta_object = db.Table('meta_object',
            db.Column("object_id", db.Integer, db.ForeignKey("object.id"), primary_key=True),
            db.Column("meta_id", db.Integer, db.ForeignKey( "meta.id"), primary_key=False)
            )


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    pic_url = db.Column(db.String(2000), nullable=False)

    # describes the relationship between rooms and objects
    # the secondary element is the table that defines the many to many relationship between the two tables
    # the back populations refers to the relationship from object to room in the defined in the Objects table 
    objects = db.relationship("Object",
            secondary=room_object,
            back_populates="rooms")
    # describes the relationship between rooms and meta
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from meta to room in the defined in the meta table
    meta_tags = db.relationship("Meta",
            secondary=meta_room,
            back_populates="room")

    # describes the relationship between rooms and user
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from user to room in the defined in the user table
    faved_rooms = db.relationship("User",
            secondary=fav_room,
            back_populates="user_rooms")
    
    # This is how the artist will print in the console, just the name
    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pic_url": self.pic_url,
            "objects": self.objects,
            "meta_tags": self.meta_tags,
            # "faved_rooms": self.faved_rooms,
        }


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sims_name = db.Column(db.String(80), unique=False, nullable=False)
    buy_url = db.Column(db.String(2000), nullable=False)
    sims_pic_url = db.Column(db.String(2000), nullable=False)
    real_pic_url = db.Column(db.String(2000), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # describes the relationship between rooms and objects
    # the secondary element is the table that defines the many to many relationship between the two tables
    # the back populations refers to the relationship from object to room in the defined in the rooms table 
    rooms = db.relationship("Room",
        secondary=room_object,
        back_populates="objects")

    # describes the relationship between Objects and meta
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from meta to Object in the defined in the meta table
    meta_tags = db.relationship("Meta",
        secondary=meta_object,
        back_populates="r_object")

    # describes the relationship between Objects and user
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from Object to user in the defined in the user table
    faved_objects = db.relationship("User",
        secondary=fav_object,
        back_populates="user_objects")

    # This is how the artist will print in the console, just the name
    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "sims_names": self.sims_name,
            "buy_url": self.buy_url,
            "sims_pic_url": self.sims_pic_url,
            "real_pic_url": self.real_pic_url,
            "price": self.price,
            "rooms": self.rooms,
            "meta_tags": self.meta_tags,
        }



# I need help understanding how to use this table because I want to have multiple tags
class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), unique=True, nullable=True)

    # describes the relationship between Object and meta
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from meta to Object in the defined in the Object table
    r_object = db.relationship("Object",
        secondary=meta_object,
        back_populates="meta_tags")

    # describes the relationship between rooms and meta
    # the secondary element is the table that defines the many to many relationship between the two tables
    # back populations refers to the relationship from meta to room in the defined in the room table
    room = db.relationship("Room",
        secondary=meta_room,
        back_populates="meta_tags")

    # This is how the artist will print in the console, just the name

    def __repr__(self):
        return self.id

    # This is how the artist will look inside the API JSON responses
    def serialize(self):
        return {
            "id": self.id,
            "description": self.tag,
            "room": self.room,
            "r_object": self.r_object,
        }

