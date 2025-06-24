from flask_restful import Resource
from flask import request,Blueprint,session
from flask_restful import Api
from models.user import User

class AuthController(Resource):

    def post(self):
        data = request.get_json()
        user=User.query.filter_by(username=data['username']).first()
        if not user :
            return {"error": "Invalid username"}, 403
        if not user.authenticate(data['password']):
            return {"error": "Invalid password"}, 403
        
        session["user_id"]=user.id
        session["username"]=user.username
        

        return user.to_dict(),403
    
auth=Blueprint('auth', __name__)
api = Api(auth)
api.add_resource(AuthController,"/login")

