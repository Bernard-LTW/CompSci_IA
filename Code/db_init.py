import sqlalchemy as db
from db_models import Base, Users, Recipe, Comments
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db_manager import DBHandler
from secure_password import *

db = DBHandler("sqlite:///recipe.sqlite")
## Create tables
Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)
