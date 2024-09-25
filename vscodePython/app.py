#app.py
from flask import Flask
from config import Config
from databaseConfig import db  # Import the shared db instance
from routes import index, insert, update, delete
from login_routes import login_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'mysecret'
   
db.init_app(app)

    
app.register_blueprint(login_bp)
        
app.add_url_rule('/', 'index', index)
app.add_url_rule('/insert', 'insert', insert, methods=['POST'])
app.add_url_rule('/update', 'update', update, methods=['POST'])
app.add_url_rule('/delete/<id>/', 'delete', delete)



if __name__ == "__main__":
    app.run(debug=True)
