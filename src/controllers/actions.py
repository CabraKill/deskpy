from flask import (Flask, request)
from src.models.desktop import Desktop
from src.models.action import Action


class Actions():
    def __init__(self, app: Flask, desktop: Desktop):
        self.app = app
        self.desktop = desktop

        @self.app.route('/actions', methods=['GET', 'POST', 'PUT', 'DELETE'])
        def _actions():
            if request.method == 'GET':
                return "get "
            if request.method == 'POST':
                responseAction = Action.fromJson(request.json)
                if responseAction.id == 0:
                    desktop.turnOff()
                    print("desligando")
                    return "desligando"
                else:
                    desktop.cancelTurnOff()
                    print("não desligando")
                    return "não desligando"

            return "DEFAULT"

        @self.app.route('/test', methods=['GET'])
        def _test0():
            return self.test()

    def test(self):
        print("test")
        return "test"
