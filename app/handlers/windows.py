import os
from app.models.desktop import Desktop
from app.models.action import Action
from app.models.error import InvalidUsage


class Windows(Desktop):
    def __init__(self):
        self.initializeMap()

    def turnOn(self, action: Action):
        msg = "Already on XD"
        print(msg)
        return msg

    def turnOff(self, action: Action):
        os.system("shutdown -s -t 3600")
        msg = "Turning off."
        print(msg)
        return msg

    def cancelTurnOff(self, action: Action):
        os.system("shutdown -a")
        return "Cancelled with success"
    
    def initializeMap(self):
        self.actionsMap = {
            0: self.turnOn,
            1: self.turnOff,
            2: self.cancelTurnOff
        }
