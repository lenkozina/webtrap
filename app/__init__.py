import os

from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
swagger = Swagger(app)
api = Api(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models

if not os.path.exists('app.db'):
    db.create_all()
migrate = Migrate(app, db)


