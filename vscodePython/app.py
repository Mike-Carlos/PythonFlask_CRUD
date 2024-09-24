from flask import Flask
from config import Config
from modelseEmployee import db
from routes import index, insert, update, delete

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/insert', 'insert', insert, methods = ['POST'])
app.add_url_rule('/update', 'update', update, methods = ['POST'])
app.add_url_rule('/delete/<id>/', 'delete', delete)


if __name__ == "__main__":
    app.run(debug=True)