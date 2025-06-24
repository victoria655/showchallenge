from .database import db
from sqlalchemy_serializer import SerializerMixin



class Episode(db.Model,SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    serialize_rules = ("-appearances.episode", "-appearances.guest")
    
    

    def __repr__(self):
        return f'<Episode {self.date},{self.number})>'