
from abc import abstractmethod

class Scene:
    def __init__(self, app) -> None:
        self.app = app 

    @abstractmethod
    def processInput(self, events, keyPressed):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def setNextScene(self, scene):
        print("Changed scene")
        self.app.changeScene(scene)
