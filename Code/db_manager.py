import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from db_models import Base, Users, Recipe, Comments
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import *
from token_management import get_username_from_token



class DBHandler:
    def __init__(self,path):
        self.engine = db.create_engine(path, echo=False)
        self.session = Session(self.engine)
        self.metadata = MetaData()
        #print(self.metadata.tables.keys())


    def login(self, username, password):
        user = self.session.query(Users).filter_by(username=username).first()
        if not user:
            return False
        return bool(check_hash(password, user.password))

    def check_user(self, username):
        return bool(self.session.query(Users).filter_by(username=username).first())

    def create_user(self, username, password):
        if not self.session.query(Users).filter_by(username=username).first():
            new_user = Users(username=username, password=hash_input(password))
            self.session.add(new_user)
            self.session.commit()
            print("User registered")
            return True
        else: return False

    def create_post(self,title, content, ingredients_json, unique_filename,token):
        user = get_username_from_token(token)
        user_id = self.session.query(Users).filter_by(username=user).first().id
        new_post = Recipe(name=title, content=content, ingredients=ingredients_json, image=unique_filename, user_id=user_id)
        self.session.add(new_post)
        self.session.commit()

    def get_all_posts(self):
        temp = self.session.query(Recipe).all()
        #append username of person who posted it
        posts = []
        for post in temp:
            posts.append([post, self.session.query(Users).filter_by(id=post.user_id).first().username])
        return posts

    def get_one_post(self, id):
        temp =  self.session.query(Recipe).filter_by(id=id).first()
        return [temp, self.session.query(Users).filter_by(id=temp.user_id).first().username]

    def get_comments_for_recipe(self, recipe_id):
        temp = self.session.query(Comments).filter_by(recipe_id=recipe_id).all()
        comments_with_username = []
        for comment in temp:
            comments_with_username.append([comment, self.session.query(Users).filter_by(id=comment.user_id).first().username])
        return comments_with_username

    def add_comment_to_recipe(self, recipe_id, username, comment_content):
        user_id = self.session.query(Users).filter_by(username=username).first().id
        new_comment = Comments(comment=comment_content, user_id=user_id, recipe_id=recipe_id)
        self.session.add(new_comment)
        self.session.commit()

    def remove_comment(self, recipe_id, comment_id, username):
        user_id = self.session.query(Users).filter_by(username=username).first().id
        comment = self.session.query(Comments).filter_by(id=comment_id, user_id=user_id, recipe_id=recipe_id).first()
        self.session.delete(comment)
        self.session.commit()

    def get_id_from_username(self, username):
        return self.session.query(Users).filter_by(username=username).first().id