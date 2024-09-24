from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone