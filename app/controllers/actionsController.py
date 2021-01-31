from flask import (Flask, request)
from app.models.desktop import Desktop
from app.models.action import Action
import json


class ActionsController():
    def __init__(self, app: Flask, desktop: Desktop):
        self.app = app
        self.desktop = desktop

        @self.app.route('/actions', methods=['GET', 'POST', 'PUT', 'DELETE'])
        def _actions():
            if request.method == 'GET':
                return "get"
            if request.method == 'POST':
                responseAction = Action.fromJson(request.json)
                return desktop.executeAction(responseAction)

            return "DEFAULT"
