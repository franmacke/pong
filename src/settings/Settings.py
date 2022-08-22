
from src.utils.PathManager import PathManager
import json
import pygame

class Settings:
    def __init__(self) -> None:
        self.settings : dict = self.loadSettings()


    def loadSettings(self):
        data = self.parseFile(PathManager.loadSettings())
        
        if not data:
            print("No hay data")
            self.settings = self.loadDefault()
            return

        return data

    def parseFile(self, fileName):
        data = None
        try:
            with open(fileName) as file:
                data = json.loads(file.read())
                # print(data)
        except:
            print("No se pudo importar el archivo settings")
        # print(data)
        return data

    def getSetting(self, settingName):
        data = self.settings.get(settingName)
        return data

    def setSetting(self, key, value):
        self.settings.update({key: value})

    def loadDefault(self):
        return {
            "volume": 0.2
        }