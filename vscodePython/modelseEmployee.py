# modelseEmployee.py
from databaseConfig import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __init__(self, name, email, phone, user_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id
