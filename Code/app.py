from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import secure_password
from db_manager import DBHandler
from token_management import create_token, check_token, get_username_from_token
from jinja2 import Environment

app = Flask(__name__)
secret_key = os.urandom(32)
app.secret_key = secret_key
db = DBHandler("sqlite:///Code/recipe.sqlite")

@app.route('/')
def landing_check():  # put application's code here
    try:
        token = session['token']
        username = get_username_from_token(token)
        if check_token(token):
            print("Token is valid")
            return redirect(url_for('dashboard'))
    except KeyError:
        print("Token is invalid or not present")
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        db = DBHandler("sqlite:///Code/recipe.sqlite")
        #print all tables in the db
        username = request.form.get('username')
        password = request.form.get('password')
        if db.login(username, password):
            session['token'] = create_token(username, 120)
            print("Login successful")
            return redirect(url_for('dashboard'))
        else:
            print("Login failed")
            flash(('Wrong username or password',"danger"))
            return redirect(url_for('login'))

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        # process form data here
        username = request.form.get('newUsername')
        password = request.form.get('newPassword')
        confirm_password = request.form.get('confirmPassword')
        if password != confirm_password:
            flash(('Passwords do not match',"danger"))
            return redirect(url_for('login'))
        elif db.check_user(username):
            flash(('Username already exists',"danger"))
            return redirect(url_for('login'))
        else:
            db.create_user(username, password)
            flash(('Registration successful. Please log in now',"success"))

            return redirect(url_for('login'))
        # do something with the form data, e.g. store it in a database
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            sort_by = request.args.get('sort_by', default='time', type=str)
            return render_template('dashboard.html', title='Dashboard', username=username)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    try:
        token = session['token']
        if request.method == 'POST':
            # process form data here
                db.create_post(title, content, code, language, username)
                flash(('Post created successfully',"success"))
                return redirect(url_for('my_profile'))
        elif request.method == 'GET':
            return render_template('new_post.html')
    except KeyError:
        return redirect(url_for('login'))





if __name__ == '__main__':
    db = DBHandler("sqlite:///Code/recipe.sqlite")
    app.run()
