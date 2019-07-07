from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'ping!'
        }

api.add_resource(UsersPing, '/users/ping')