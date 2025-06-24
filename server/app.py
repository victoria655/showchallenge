import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from dotenv import load_dotenv


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from models.database import db


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config) #Load configuration from Config class

db.init_app(app)  # Initialize SQLAlchemy with the Flask app
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Defer blueprint imports to avoid circular imports
def register_blueprints():
    from controllers.auth_controller import auth_bp
    from controllers.guest_controller import guest_bp
    from controllers.episode_controller import episode_bp
    from controllers.appearance_controller import appearance_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

# Register blueprints 
register_blueprints()

if __name__ == '__main__':
    app.run(debug=True)