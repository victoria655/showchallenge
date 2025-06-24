from .database import db
from sqlalchemy_serializer import SerializerMixin




class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(500), nullable=True)

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')


    serialize_rules = ("-appearances.guest", "-appearances.episode")    
   

    def __repr__(self):
        return f'<Guest {self.name} ,{self.occupation}>'