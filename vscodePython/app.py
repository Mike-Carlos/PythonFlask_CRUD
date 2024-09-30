#app.py
from flask import Flask
from config import Config
from databaseConfig import db  # Import the shared db instance
from routes import delete_multiple, index, insert, update, delete, dashboard_data, dashboard
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
app.add_url_rule('/delete_multiple/<ids>','delete_multiple',delete_multiple,methods=['GET'])
app.add_url_rule('/dashboard', 'dashboard', dashboard)
app.add_url_rule('/dashboard_data', 'dashboard_data',dashboard_data)

if __name__ == "__main__":
    app.run(debug=True)
