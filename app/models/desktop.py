from app.models.action import Action


class Desktop():
    SHUTDOWNTIME = 300
    
    def __init__(self):
        self.initializeMap()

    def initializeMap(self):
        self.actionsMap = {
            0: self.turnOn,
            1: self.turnOff,
            2: self.cancelTurnOff
        }

    def turnOn(self, action: Action):
        raise NotImplementedError()

    def turnOff(self, action: Action):
        raise NotImplementedError()

    def cancelTurnOff(self, action: Action):
        raise NotImplementedError()

    def executeAction(self, action: Action):
        return self.actionsMap[action.id](action)
