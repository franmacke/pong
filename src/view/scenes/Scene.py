
from abc import abstractmethod

class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.prevScene = None
        self.nextScene = None

    @abstractmethod
    def processInput(self, events, keyPressed):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def goToNextScene(self):
        print("Changed scene")
        self.app.changeScene(self.nextScene)

    def goToPrevScene(self):
        self.app.changeScene(self.prevScene)

    def setNextScene(self, scene):
        self.nextScene = scene

    def savePreviusScene(self, scene):
        self.prevScene = scene