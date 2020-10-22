from flask import Flask


def create_app():
    app: Flask = Flask(__name__)
    return app
