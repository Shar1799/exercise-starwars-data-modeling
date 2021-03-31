import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#Usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(250), nullable=False)
    password_user = Column(String(250), nullable=False)
    firstname_user = Column(String(250), nullable=False)
    lastname_user = Column(String(250), nullable=False)
    email_user = Column(String(250), nullable=False)

#Favoritos
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters_fav = Column(Integer, ForeignKey('characters.id'))
    planets_fav = Column(Integer, ForeignKey('planets.id'))
    user_fav = Column(Integer, ForeignKey('user.id'))

#Personajes 
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name_character = Column(String(250),nullable=True)
    gender = Column(String(250))
    height = Column(Integer)
    age = Column(Integer)
    description_character = Column(String(250))

#Planetas
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250))
    population = Column(Integer)
    surface = Column(Integer)
    description_planet = Column(String(250))

#Retornar
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')