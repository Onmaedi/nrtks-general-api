from flask import Flask
from dynaconf import FlaskDynaconf


def init_configuration(app: Flask) -> None:
    FlaskDynaconf(app)
    app.config.load_extensions()
