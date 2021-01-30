import os
from src.models.desktop import Desktop


class Windows(Desktop):
    def __init__(self):
        pass

    def turnOn(self):
        print("Not implemented")

    def turnOff(self):
        os.system("shutdown -s -t 3600")

    def cancelTurnOff(self):
        os.system("shutdown -a")
