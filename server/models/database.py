from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metata = MetaData()
db = SQLAlchemy(metadata=metata)
