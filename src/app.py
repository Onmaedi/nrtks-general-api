from flask import Flask
from dotenv import load_dotenv
from dynaconf import FlaskDynaconf
from .config import configuration


def create_app():
    load_dotenv()
    app: Flask = Flask(__name__)
    configuration.init_configuration(app)
    return app
