#Install dependencies:
pip install Flask
pip install Flask-SQLAlchemy
pip install PyMySQL  # If you're using MySQL
pip install Werkzeug

#Configure config.py
(Configure your database connection.)
Example: SQLALCHEMY_DATABASE_URI = 'mysql://enter_username:enter_password''@localhost/enter_database_name'


#Run App 
(Ensure that you have MySQL server running and that you have created the necessary database if you're using MySQL.)
flask run OR python app.py


