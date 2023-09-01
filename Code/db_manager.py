import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from db_models import Base, Users, Recipe, Comments
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import *



class DBHandler:
    def __init__(self,path):
        self.engine = db.create_engine(path, echo=True)
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
