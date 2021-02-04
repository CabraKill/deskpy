from flask import (Flask, request)
from app.models.desktop import Desktop
from app.models.action import Action
import json


class ActionsController():
    def __init__(self, app: Flask, desktop: Desktop):
        self.app = app
        self.desktop = desktop

        @self.app.route('/actions/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
        def _actions(id):
            if request.method == 'GET':
                responseAction = Action.fromId(id)
                return desktop.executeAction(responseAction)
            if request.method == 'POST':
                responseAction = Action.fromJson(request.json)
                return desktop.executeAction(responseAction)

            return "DEFAULT"
