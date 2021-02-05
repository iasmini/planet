from sqlalchemy_serializer import SerializerMixin

from app import db


class Planet(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, index=True)
    rotation_period = db.Column(db.String, nullable=True)
    orbital_period = db.Column(db.String, nullable=True)
    diameter = db.Column(db.String, nullable=True)
    climate = db.Column(db.String, nullable=True, index=True)
    gravity = db.Column(db.String, nullable=True)
    terrain = db.Column(db.String, nullable=True)
    surface_water = db.Column(db.String, nullable=True)
    population = db.Column(db.Integer, nullable=True)
