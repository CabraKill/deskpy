import os
from app.models.desktop import Desktop
from app.models.action import Action
from app.models.error import InvalidUsage
from flask_api import status


class Windows(Desktop):
    

    def __init__(self):
        self.initializeMap()

    def turnOn(self, action: Action):
        msg = "Already on XD"
        return msg

    def turnOff(self, action: Action):
        os.system(f"shutdown -s -t {self.SHUTDOWNTIME}")
        msg = "Turning off."
        return msg

    def cancelTurnOff(self, action: Action):
        try:
            os.system("shutdown -a")
        except Exception as e:
            raise InvalidUsage(
                f"Unable to stop shutting down: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return "Cancelled with success"
