#login_routes
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from model_user import User
from databaseConfig import db

login_bp = Blueprint('login', __name__)


@login_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash('You have been logged out!')
    return redirect(url_for('login.login'))



@login_bp.route('/login',methods=['GET','POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
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
            flash('Username already exists.')
        else:
            User.create_user(username, password)
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login.login')) 

    return render_template('register.html')

@login_bp.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        
        user = User.query.get(session.get('user_id'))
        
        if user and user.check_password(current_password):
            user.set_password(new_password)  
            db.session.commit()
            flash('Password changed successfully!')
            return redirect(url_for('index'))
        else:
            flash('Current password is incorrect.')
    
    return render_template('change_password.html') 