#external imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local import
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__ , instance_relative_config=True) #changes the loading via filenames to be relative to the instance path
    app.config.from_object(app_config[config_name]) #Updates the values from the given object : Load Configuration Defaults
    app.config.from_pyfile('config.py') #Updates the values in the config from a Python file

    db.init_app(app)


    migrate = Migrate(app, db)

    from app import model
    from .NSE import nse as nse_blueprint
    app.register_blueprint(nse_blueprint)

    return app

