#routes.py
from flask import flash, redirect, render_template, request, session, url_for
from modelseEmployee import Data, db
from model_user import User


def index():
    if 'user_id' not in session:
        
        return redirect(url_for('login.login'))
    
    current_user = session.get('username')
    
    all_data = Data.query.all()
    all_users = User.query.all()
    return render_template('index.html', employees = all_data, current_user=current_user, users=all_users)


def insert():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']  
        password = request.form['password']  
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists.')
        else:
            new_user = User.create_user(username, password)
        
        my_data = Data(name, email, phone, user_id=new_user.id)
        db.session.add(my_data)
        db.session.commit()
        
        flash("Employee Added Successfully!")
        
        return redirect(url_for('index'))


def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
         
        db.session.commit()
        
        flash("Employee Updated Successfully!")
        
        return redirect(url_for('index'))
        

def delete(id):
    my_data = Data.query.get(id)
    
    if my_data:
        # Get the user associated with the employee
        user_id = my_data.user_id
        
        # Delete the associated Data entries
        associated_data = Data.query.filter_by(user_id=user_id).all()
        for data_entry in associated_data:
            db.session.delete(data_entry)
        
        # Delete the user
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)

        # Finally delete the specific employee record
        db.session.delete(my_data)

        db.session.commit()
        flash("Employee and associated user removed!")
    else:
        flash("Employee not found.")
    
    return redirect(url_for('index'))