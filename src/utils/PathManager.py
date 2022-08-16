from pathlib import Path
import os


HOME_DIR = os.getcwd()

class PathManager:

    @staticmethod
    def loadFont(font):
        return Path(HOME_DIR, "assets/fonts/", f"{font}.ttf")
