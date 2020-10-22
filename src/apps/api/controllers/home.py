from flask import jsonify, current_app
from flask_restful import Resource


class HomeController(Resource):
    def get(self):
        return jsonify({
            "message": current_app.config["TITLE"],
            "web-site": "https://neuroteks.com/"
        })
