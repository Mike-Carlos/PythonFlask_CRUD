# model_user.py
from databaseConfig import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def create_user(username, password):
        new_user = User(username=username)
        new_user.set_password(password)  # Set the hashed password
        db.session.add(new_user)
        db.session.commit()