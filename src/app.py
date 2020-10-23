from flask import Flask
# from .config.configuration import init_configuration


def create_app():
    app: Flask = Flask(__name__)

    @app.route("/")
    def _():
        return "Test route"

    # init_configuration(app)
    return app
