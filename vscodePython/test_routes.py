# # test_routes.py

# import pytest
# from flask import Flask, session
# from app import app, db
# from model_user import User
# from modelseEmployee import Data

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite for tests
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()  # Create database tables
#         yield client
#         with app.app_context():
#             db.drop_all()  # Cleanup after tests

# @pytest.fixture
# def create_user():
#     def _create_user(username, password):
#         user = User(username=username)
#         user.set_password(password)  # Assume this method hashes the password
#         db.session.add(user)
#         db.session.commit()
#         return user
#     return _create_user

# def test_index_redirects(client):
#     """Test index redirects to login if not logged in."""
#     response = client.get('/')
#     assert response.status_code == 302
#     assert b'login' in response.data

# def test_login(client, create_user):
#     """Test successful login."""
#     user = create_user('testuser', 'password')
    
#     response = client.post('/login', data={
#         'username': 'testuser',
#         'password': 'password'
#     })
    
#     with client:
#         assert session['user_id'] == user.id
#         assert session['username'] == user.username
#         assert b'Login Successful!' in response.data

# def test_login_failed(client):
#     """Test login fails with incorrect credentials."""
#     response = client.post('/login', data={
#         'username': 'invaliduser',
#         'password': 'wrongpassword'
#     })
    
#     assert b'Login failed. Check your credentials.' in response.data

# def test_insert_employee(client, create_user):
#     """Test inserting a new employee."""
#     user = create_user('testuser', 'password')
#     session['user_id'] = user.id
#     session['username'] = user.username

#     response = client.post('/insert', data={
#         'name': 'John Doe',
#         'email': 'john@example.com',
#         'phone': '1234567890',
#         'username': 'johndoe',
#         'password': 'password123'
#     })
    
#     assert b'Employee Added Successfully!' in response.data

#     employee = Data.query.filter_by(name='John Doe').first()
#     assert employee is not None

# def test_update_employee(client, create_user):
#     """Test updating an employee's information."""
#     user = create_user('testuser', 'password')
#     session['user_id'] = user.id
#     session['username'] = user.username

#     employee = Data(name='John Doe', email='john@example.com', phone='1234567890', user_id=user.id)
#     db.session.add(employee)
#     db.session.commit()

#     response = client.post('/update', data={
#         'id': employee.id,
#         'name': 'Jane Doe',
#         'email': 'jane@example.com',
#         'phone': '0987654321'
#     })

#     assert b'Employee Updated Successfully!' in response.data
#     updated_employee = Data.query.get(employee.id)
#     assert updated_employee.name == 'Jane Doe'
#     assert updated_employee.email == 'jane@example.com'

# def test_delete_employee(client, create_user):
#     """Test deleting an employee."""
#     user = create_user('testuser', 'password')
#     session['user_id'] = user.id
#     session['username'] = user.username

#     employee = Data(name='John Doe', email='john@example.com', phone='1234567890', user_id=user.id)
#     db.session.add(employee)
#     db.session.commit()

#     response = client.get(f'/delete/{employee.id}/')

#     assert b'Employee Removed!' in response.data
#     assert Data.query.get(employee.id) is None

# def test_logout(client, create_user):
#     """Test logout functionality."""
#     user = create_user('testuser', 'password')
#     with client:
#         session['user_id'] = user.id
#         session['username'] = user.username

#         response = client.get('/logout')
#         assert b'You have been logged out!' in response.data
#         assert 'user_id' not in session
#         assert 'username' not in session
