from .episode_controller import EpisodeController
from .appearance_controller import AppearanceController
from .guest_controller import GuestController
from flask import Blueprint
from flask_restful import Api

def controllers_blueprint(name,model):
    bp= Blueprint(name, __name__)
    api = Api(bp)

    api.add_resource(EpisodeController,"/",resource_class_kwargs=
    {'model': model})
    api.add_resource(AppearanceController,"/appearance",resource_class_kwargs=
    {'model': model})
    api.add_resource(GuestController,"/guest",resource_class_kwargs=
    {'model': model})   
    return bp
    