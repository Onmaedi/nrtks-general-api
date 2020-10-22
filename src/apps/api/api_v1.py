from flask import Flask, Blueprint
from flask_restful import Api
from .controllers.home import HomeController


app_blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api = Api(app_blueprint)

api.add_resource(HomeController, "/")


def init_app(app: Flask):
    app.register_blueprint(app_blueprint)
