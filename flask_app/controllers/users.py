from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def dashboard():
    allUsers = User.getAllUsers()
    return render_template('dashboard.html', users= allUsers)


@app.route('/createUser', methods=['POST'])
def createUser():
    data = {
        'email': request.form['email'],
        'name': request.form['name'],
        'lastName': request.form['lastName']
    }
    User.create_user(data)
    return redirect('/')