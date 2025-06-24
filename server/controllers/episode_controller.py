from flask_restful import Resource
from flask import request, jsonify
from models.episode import Episode
from models.database import db


class EpisodeController(Resource):
    def __init__(self, model):
        super().__init__()
        self.model = model 
         
    def get(self):
        """
        Get all episodes.
        """
        episodes = Episode.query.all()
        return jsonify([{
            'id': episode.id,
            'date': episode.date.isoformat() if episode.date else None,
            'number': episode.number
        } for episode in episodes])

    def post(self):
        """
        Create a new episode.
        """
        data = request.get_json()
        new_episode = Episode(
            date=data.get('date'),
            number=data['number']
        )
        db.session.add(new_episode)
        db.session.commit()
        return jsonify({'message': 'Episode created successfully', 'id': new_episode.id}), 201
    def patch(self, episode_id):
        """
        Update an existing episode.
        """
        data = request.get_json()
        episode = Episode.query.get_or_404(episode_id)

        if 'date' in data:
            episode.date = data['date']
        if 'number' in data:
            episode.number = data['number']

        db.session.commit()
        return jsonify({'message': 'Episode updated successfully'})
    
    def delete(self, episode_id):
        """
        Delete an episode.
        """
        episode = Episode.query.get_or_404(episode_id)
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Episode deleted successfully'})