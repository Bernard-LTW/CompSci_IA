from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"
    id: Column[int] = Column(Integer, primary_key=True)
    username: Column[str] = Column(String(20), unique=True)
    password: Column[str] = Column(String(200))


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"


class Recipe(Base):
    __tablename__ = "recipes"
    id: Column[int] = Column(Integer, primary_key=True)
    name: Column[str] = Column(String(20))
    description: Column[str] = Column(String(2000))
    ingredients: Column[str] = Column(String(2000))
    instructions: Column[str] = Column(String(2000))
    image: Column[str] = Column(String(2000))
    user_id: Column[int] = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Recipe(id={self.id!r}, name={self.name!r})"


class Comments(Base):
    __tablename__ = "comments"
    id: Column[int] = Column(Integer, primary_key=True)
    comment: Column[str] = Column(String(2000))
    user_id: Column[int] = Column(Integer, ForeignKey("users.id"))
    recipe_id: Column[int] = Column(Integer, ForeignKey("recipes.id"))

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, comment={self.comment!r})"
