import requests
from flask_api import status
from app.models.action import Action
class GoDriver():
    def __init__(self, actionsMap: dict, deviceName: str,):
        self.actionsMap = actionsMap
        self.deviceName = deviceName

    def sendActions(self, link: str):
        jsonMap = {
            "name": self.deviceName,
            "type": "0",
            "actions": map(Action.toJson, self.actionsMap),

        }
        response = requests.post(link, json=jsonMap)
        if response.status_code != status.HTTP_200_OK:
            print("Unable to register in goHome")
        else:
            print("Registered in goHome")
        

        
