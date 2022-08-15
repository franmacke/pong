from abc import abstractmethod

from src.model.position.Position import Position

class Positionable:
    
    @abstractmethod
    def setPosition(self, position):
        pass

    @abstractmethod
    def getPosition(self):
        pass