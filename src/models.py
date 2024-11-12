import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.email

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "climate": self.climate
        }

class People(db.Model):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    eye_color = Column(String(250))
    mass = Column(Integer, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.id

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "eye_color": self.eye_color,
            "mass": self.mass
        }


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey(Planet.id), nullable=True)
    id_user = Column(Integer, ForeignKey(User.id), nullable=False)
    id_people = Column(Integer, ForeignKey(People.id), nullable=True)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def dict(self):
        return {   
            "id": self.id,
            "id_planet": self.id_planet,
            "id_user": self.id_user,
            "id_character": self.id_character
        }