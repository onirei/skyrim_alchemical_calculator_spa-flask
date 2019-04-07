from sac_app import db

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(128))
    id_object = db.Column(db.String(128))
    attribute_1 = db.Column(db.String(128))
    attribute_2 = db.Column(db.String(128))
    attribute_3 = db.Column(db.String(128))
    attribute_4 = db.Column(db.String(128))

class Negative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(128))

class Positive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(128))
