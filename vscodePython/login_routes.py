#login_routes
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from model_user import User

login_bp = Blueprint('login', __name__)


@login_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login Successful!')
            print(session.get('user_id'))

            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your credentials.')
            
    return render_template('login.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
        else:
            User.create_user(username, password)
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login.login')) 

    return render_template('register.html')
