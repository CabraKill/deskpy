import json


class Action():
    def __init__(self, id: int, typeAction=0, name=""):
        self.id = id
        self.typeAction = typeAction
        self.name = name

    @staticmethod
    def fromJson(body: dict):
        jsonMap = body
        return Action(jsonMap.get("id"), jsonMap.get("typeAction"), jsonMap.get("name"))
    
    @staticmethod
    def fromId(id: int):
        return Action(id)

    @staticmethod
    def toJson(actionObject):
        if(type(actionObject) is not Action):
            raise Exception(f"The type {type(actionObject)} is not an Action")
        return json.dumps({
            "id": actionObject.id,
            "type": actionObject.type,

        })
