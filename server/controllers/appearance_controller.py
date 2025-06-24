from flask_restful import Resource
from flask import request, jsonify
from models.database import db
from models.appearance import Appearance


class AppearanceController(Resource):
    def __init__(self, model):
        super().__init__()
        self.model = model              

    def get(self):
        """
        Get all appearances.
        """
        
        appearances = Appearance.query.all()
        return jsonify([{
            'id': appearance.id,
            'rating_id': appearance.rating_id,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id
        } for appearance in appearances])

    def post(self):
        """
        Create a new appearance.
        """
        
        data = request.get_json()
        new_appearance = Appearance(
            rating_id=data['rating_id'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify({'message': 'Appearance created successfully', 'id': new_appearance.id}), 201
    
    def patch(self, appearance_id):
        """
        Update an existing appearance.
        """
       
        data = request.get_json()
        appearance = Appearance.query.get_or_404(appearance_id)
        
        if 'rating_id' in data:
            appearance.rating_id = data['rating_id']
        if 'guest_id' in data:
            appearance.guest_id = data['guest_id']
        if 'episode_id' in data:
            appearance.episode_id = data['episode_id']
        
        db.session.commit()
        return jsonify({'message': 'Appearance updated successfully'})
    
    def delete(self, appearance_id):
        """
        Delete an appearance.
        """
       
        appearance = Appearance.query.get_or_404(appearance_id)
        db.session.delete(appearance)
        db.session.commit()
        return jsonify({'message': 'Appearance deleted successfully'})

