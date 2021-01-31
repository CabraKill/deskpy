from app.models.action import Action
from app.models.actionList import ActionList


class Desktop():
    SHUTDOWNTIME = 300

    def __init__(self):
        self.initializeMap()

    def initializeMap(self):
        self.actionsMap = {
            0: {
                "name": "Turn On",
                "type": ActionList.ON,
                "action": self.turnOn
            },
            1: {
                "name": "Turn Off",
                "type": ActionList.OFF,
                "action": self.turnOff
            },
            2: {
                "name": "Cancel Turn off",
                "type": ActionList.ON,
                "action": self.cancelTurnOff
            }
             
        }

    def turnOn(self, action: Action):
        raise NotImplementedError()

    def turnOff(self, action: Action):
        raise NotImplementedError()

    def cancelTurnOff(self, action: Action):
        raise NotImplementedError()

    def executeAction(self, action: Action):
        return self.actionsMap[action.id]["action"](action)
