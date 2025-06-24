from .database import db
from sqlalchemy.ext import hybrid
import re
from flask_bcrypt import Bcrypt
from sqlalchemy_serializer import SerializerMixin

bcrypt= Bcrypt()

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    


    @hybrid.hybrid_property
    def password(self):
        return "you cannot access the password directly"
    @password.setter
    def password(self, plain_text):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if not re.match(pattern, plain_text):
            raise ValueError("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        
        self.password_hash =bcrypt.generate_password_hash(plain_text).decode('utf-8')
        
    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

        

    def __repr__(self):
        return f'<User {self.username}>'