from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# association table 
# association_table = db.Table('association',
#     db.Column("sister_id", db.Integer, ForeignKey("sister.id"), primary_key=True),
#     db.Column("brother_id", db.Integer, ForeignKey("brother.id"), primary_key=True)
# )

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

fav_room = db.Table('fav_room',
    db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True))

fav_item = db.Table('fav_item',
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True))

item_room = db.Table('item_room',
    db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
    db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True)
)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    pic_url = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)


# This error
    items = db.relationship("Item",
                    secondary= item_room,
                    back_populates="Room") 

    def __repr__(self):
        return self.name
        
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pic_url": self.pic_url,
            "price": self.price,
        }

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    buy_url = db.Column(db.String(500), nullable=False)
    sims_pic_url = db.Column(db.String(500), nullable=False)
    real_pic_url = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    rooms = db.relationship("Room",
                    secondary= item_room,
                    back_populates="item") 

    def __repr__(self):
        return self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "buy_url": self.buy_url,
            "pic_url": self.pic_url,
            "price": self.price,
        }


meta_room = db.Table('meta_room',
    db.Column("meta_id", db.Integer, db.ForeignKey("meta.id"), primary_key=True),
    db.Column("room_id", db.Integer, db.ForeignKey("room.id"), primary_key=True)
)

meta_item = db.Table('meta_item',
    db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
    db.Column("meta_id", db.Integer, db.ForeignKey("meta.id"), primary_key=True)
)


class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    style = db.Column(db.String(80), nullable=False)
    room_type = db.Column(db.String(80), nullable=False)
    item_type = db.Column(db.String(80), nullable= False)
    age_group = db.Column(db.String(80), nullable=False)
  
     
    Item = db.relationship("Item",
                    secondary= meta_item,
                    back_populates="item") 
                
    Room = db.relationship("Room",
                    secondary= meta_room,
                    back_populates="room") 

   

    # This is how the artist will print in the console, just the name
    def __repr__(self):
        return self.name

    # This is how the artist will look inside the API JSON responses 
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "style": self.style,
            "room_type": self.room_type,
            "age_group": self.age_group,
        }

