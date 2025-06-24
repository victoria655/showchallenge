from .database import db
from sqlalchemy_serializer import SerializerMixin


class Appearance(db.Model,SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating_id = db.Column(db.Integer,db.CheckConstraint('rating_id > 0 AND rating_id < 5'),nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))


    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    serialize_rules=("-guest.appearances", "-episode.appearances")
    def __repr__(self):
        return f'<Appearance {self.rating_id}>'