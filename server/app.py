from flask import Flask,session,request
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from models.database import db
from models import Appearance,Episode, Guest,User
from controllers import controllers_blueprint
from controllers.auth_controller import  auth

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)
bcrypt = Bcrypt(app)
protected_routes = [
    ("POST", "/appearances"),
    ("DELETE", "/episodes/<int:id>")
]
@app.before_request
def isAuthenticated():
    if "uid" not in session and any(
        request.method == method and request.path.startswith(path)
        for method, path in protected_routes
    ):
        return {"error": "You must be logged in to access this resource"}, 403


crud_routes =[
    {"name": "appearance", "model": Appearance},
    {"name": "episode", "model": Episode},
    {"name": "guest", "model": Guest},
    {"name": "user", "model": User}
]

for route in crud_routes:
    shows = controllers_blueprint(**route)
    app.register_blueprint(shows, url_prefix=f"/{route['name']}")


app.register_blueprint(auth, url_prefix="/auth")




