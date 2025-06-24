from flask_restful import Resource
from flask import request, jsonify
from models.guest import Guest
from models.database import db


class GuestController(Resource):


    def __init__(self, model):
        super().__init__()
        self.model = model     
    def get(self):
        """
        Get all guests.
        """
        guests = Guest.query.all()
        return jsonify([{
            'id': guest.id,
            'name': guest.name,
            'slug': guest.slug,
            'image_url': guest.image_url
        } for guest in guests])

    def post(self):
        """
        Create a new guest.
        """
        data = request.get_json()
        new_guest = Guest(
            name=data['name'],
            slug=data['slug'],
            image_url=data.get('image_url')
        )
        db.session.add(new_guest)
        db.session.commit()
        return jsonify({'message': 'Guest created successfully', 'id': new_guest.id}), 201
    def patch(self, guest_id):
        """     
        Update an existing guest.
        """
        data = request.get_json()
        guest = Guest.query.get_or_404(guest_id)

        if 'name' in data:
            guest.name = data['name']
        if 'slug' in data:
            guest.slug = data['slug']
        if 'image_url' in data:
            guest.image_url = data.get('image_url')

        db.session.commit()
        return jsonify({'message': 'Guest updated successfully'})
    def delete(self, guest_id):
        """
        Delete a guest.
        """
        guest = Guest.query.get_or_404(guest_id)
        db.session.delete(guest)
        db.session.commit()
        return jsonify({'message': 'Guest deleted successfully'})