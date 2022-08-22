from pathlib import Path
import os, sys


HOME_DIR = os.getcwd()


class PathManager:  

    @staticmethod
    def loadFont(font):
        return os.path.join(os.path.abspath('.'), f"assets/fonts/{font}.ttf")

    @staticmethod
    def loadSound(file):
        return os.path.join(os.path.abspath('.'), f"assets/sounds/{file}.mp3")
        
    @staticmethod
    def loadBackground(file):
        return os.path.join(os.path.abspath('.'), f"assets/background/{file}.jpg")

    @staticmethod
    def loadButton(file):
        return os.path.join(os.path.abspath('.'), f"assets/buttons/{file}.png")

    @staticmethod
    def loadSettings():
        return os.path.join(os.path.abspath('.'), "src/settings/settings.txt")