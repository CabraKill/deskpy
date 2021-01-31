from flask import (Flask, request)
from app.models.desktop import Desktop
from app.models.action import Action
from app.models.error import InvalidUsage
from flask import jsonify


class Actions():
    def __init__(self, app: Flask, desktop: Desktop):
        self.app = app
        self.desktop = desktop

        @self.app.route('/actions', methods=['GET', 'POST', 'PUT', 'DELETE'])
        def _actions():
            # if(not error):
            #     response = jsonify(error.to_dict())
            #     response.status_code = error.status_code
            #     return response
            if request.method == 'GET':
                return "get"
            if request.method == 'POST':
                responseAction = Action.fromJson(request.json)
                return desktop.executeAction(responseAction)

            return "DEFAULT"

        @self.app.errorhandler(InvalidUsage)
        def handle_invalid_usage(error):
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

    def test(self):
        print("test")
        return "test"
