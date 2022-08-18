from pathlib import Path
import os


HOME_DIR = os.getcwd()

class PathManager:

    @staticmethod
    def loadFont(font):
        return Path(HOME_DIR, "assets/fonts/", f"{font}.ttf")

    @staticmethod
    def loadSound(file):
        return Path(HOME_DIR, "assets/sounds/", f"{file}.mp3")
        
    @staticmethod
    def loadBackground(file):
        return Path(HOME_DIR, "assets/background/", f"{file}.jpg")

    @staticmethod
    def loadButton(file):
        return Path(HOME_DIR, "assets/buttons/", f"{file}.png")