from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er
db = SQLAlchemy()


Base = declarative_base()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Fav_room(db.Model):
    name = db.Column(db.String(80), nullable=False)
    User_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    Room_id = db.Column(db.Integer, db.ForeignKey("Room.id"), nullable=False)
    

class Fav_item(db.Model):
    name = db.Column(db.String(80), nullable=False)
    User_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    Sims_item_id = db.Column(db.Integer, db.ForeignKey("Sims_item.id"), nullable=False)
    


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Sims_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Item_room(db.Model):
    name = db.Column(db.String(80), nullable=False)
    Room_id = db.Column(db.Integer, db.ForeignKey("Room.id"), nullable=False)
    Sims_item_id = db.Column(db.Integer, db.ForeignKey("Item.id"), nullable=False)
    
    def __repr__(self):
        return self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

Copy
class Real_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    Sims_item_id = db.Column(db.Integer, db.ForeignKey("Sims_item.id"), nullable=False)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "records": list(map(lambda x: x.serialize(), self.records))
        }


class Meta_room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Room_id = db.Column(db.Integer, db.ForeignKey("Room.id"), nullable=False)
    

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "records": list(map(lambda x: x.serialize(), self.records))
        }

class Meta_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    Sims_item_id = db.Column(db.Integer, db.ForeignKey("Sims_item.id"), nullable=False)


    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "records": list(map(lambda x: x.serialize(), self.records))
        }


class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    Meta_room_id = db.Column(db.Integer, db.ForeignKey("Meta_room.id"), nullable=False)
    Meta_item_id = db.Column(db.Integer, db.ForeignKey("Meta_item.id"), nullable=False)

    # This is how the artist will print in the console, just the name
    def __repr__(self):
        return self.name

    # This is how the artist will look inside the API JSON responses 
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

