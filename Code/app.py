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


if __name__ == '__main__':
    db = DBHandler("sqlite:///recipe.sqlite")
    app.run()
