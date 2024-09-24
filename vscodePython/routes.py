from flask import flash, redirect, render_template, request, url_for
from modelseEmployee import Data, db


def index():
    all_data = Data.query.all()
    return render_template('index.html', employees = all_data)


def insert():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        my_data = Data(name, email, phone)
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
    db.session.delete(my_data)
    db.session.commit()
        
    flash("Employee Removed!")    
    return redirect(url_for('index'))