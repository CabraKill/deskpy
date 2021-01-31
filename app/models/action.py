import json


class Action():
    def __init__(self, id, name=""):
        self.id = id
        self.name = name

    @staticmethod
    def fromJson(body):
        jsonMap = body  # json.loads(json)
        return Action(jsonMap["id"], jsonMap["name"])
