import json
import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory

from Code.db_models import Users
from db_manager import DBHandler
from token_management import create_token, check_token, get_username_from_token

app = Flask(__name__)
secret_key = os.urandom(32)
app.secret_key = secret_key
db = DBHandler("sqlite:///Code/recipe.sqlite")
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UPLOADS_PATH = os.path.join(BASE_DIR, 'uploads')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        # print all tables in the db
        username = request.form.get('username')
        password = request.form.get('password')
        if db.login(username, password):
            session['token'] = create_token(username, 120)
            print("Login successful")
            return redirect(url_for('dashboard'))
        else:
            print("Login failed")
            flash(('Wrong username or password', "danger"))
            return redirect(url_for('login'))


@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        # process form data here
        username = request.form.get('newUsername')
        password = request.form.get('newPassword')
        confirm_password = request.form.get('confirmPassword')
        if password != confirm_password:
            flash(('Passwords do not match', "danger"))
            return redirect(url_for('login'))
        elif db.check_user(username):
            flash(('Username already exists', "danger"))
            return redirect(url_for('login'))
        else:
            db.create_user(username, password)
            flash(('Registration successful. Please log in now', "success"))

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
            posts = db.get_all_posts()
            return render_template('dashboard.html', title='Dashboard', username=username,posts=posts)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))


@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    try:
        token = session['token']

        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            ingredient_names = request.form.getlist('ingredient_name[]')
            ingredient_amounts = request.form.getlist('ingredient_amount[]')
            ingredient_units = request.form.getlist('ingredient_unit[]')

            ingredients = zip(ingredient_names, ingredient_amounts, ingredient_units)
            ingredients_dict_list = [
                {
                    "name": ingredient_name,
                    "amount": ingredient_amount,
                    "unit": need_description
                }
                for ingredient_name, ingredient_amount, need_description in ingredients
            ]
            ingredients_json = json.dumps(ingredients_dict_list)

            uploaded_file = request.files.get('uploaded_image')

            if uploaded_file and uploaded_file.filename != '':
                if allowed_file(uploaded_file.filename):
                    # Generate unique filename using timestamp
                    unique_filename = f"{int(time.time())}_{uploaded_file.filename}"
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                    uploaded_file.save(filepath)
                    print(f"Image saved as: {filepath}")
                else:
                    print("Invalid file type.")
                    return "Invalid file type.", 400
            else:
                unique_filename = "No file"
            db.create_post(title, content, ingredients_json, unique_filename,token)
            return redirect(url_for('dashboard'))

        elif request.method == 'GET':
            return render_template('new_post.html')

    except KeyError:
        return redirect(url_for('login'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADS_PATH, filename)

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    # Check if the token exists in the session
    token = session.get('token')
    if token and check_token(token):
        username = get_username_from_token(token)
        user_id = db.get_id_from_username(username)
        recipe_data = db.get_one_post(recipe_id)
        if recipe_data:
            recipe_details = recipe_data[0]
            temp_ingredients = json.loads(recipe_details.ingredients)
            comments = db.get_comments_for_recipe(recipe_id)
            #append username to comments
            return render_template('recipe.html', title='Recipe', recipe=recipe_details, ingredients=temp_ingredients, poster_username=recipe_data[1], comments=comments, username=username)
        else:
            return "Recipe not found", 404
    return redirect(url_for('login'))

@app.route("/recipe/<int:recipe_id>/add_comment", methods=['POST'])
def add_comment(recipe_id):
    token = session.get('token')
    if token and check_token(token):
        username = get_username_from_token(token)
        comment_content = request.form.get('comment_content')
        db.add_comment_to_recipe(recipe_id, username, comment_content)
        return redirect(url_for('recipe', recipe_id=recipe_id))
    return redirect(url_for('login'))

@app.route("/recipe/<int:recipe_id>/delete_comment/<int:comment_id>/", methods=['GET'])
def remove_comment(recipe_id, comment_id):
    token = session.get('token')
    if token and check_token(token):
        username = get_username_from_token(token)
        db.remove_comment(recipe_id, comment_id, username)
        return redirect(url_for('recipe', recipe_id=recipe_id))
    return redirect(url_for('login'))

@app.route("/search", methods=['GET', 'POST'])
def search():
    token = session.get('token')
    if token and check_token(token):
        username = get_username_from_token(token)
        if request.method == 'POST':
            search_query = request.form.get('search_query')
            posts = db.search(search_query)
            return render_template('search.html', title='Dashboard', username=username, search_results=posts)
        elif request.method == 'GET':
            return render_template('search.html', username=username)
    return redirect(url_for('login'))

@app.route("/profile/<username>")
def profile(username):
    token = session.get('token')
    if token and check_token(token):
        username = get_username_from_token(token)
        posts = db.get_post_from_user(username)
        return render_template('profile.html', title='Profile', username=username, posts=posts)
    return redirect(url_for('login'))


if __name__ == '__main__':
    db = DBHandler("sqlite:///Code/recipe.sqlite")
    app.run()
