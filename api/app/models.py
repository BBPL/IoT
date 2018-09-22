from app import db

class Satellite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String)

   