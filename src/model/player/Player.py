
from src.model.observer.Observable import Observable
from src.model.position.Position import Position
from src.model.positionable.Positionable import Positionable
from src.model.sizable.Sizable import Sizable
from src.model.size.Size import Size

class Player(Positionable, Observable, Sizable):
    def __init__(self) -> None:
        self.speed = 15
        self.position = Position(0,0)
        self.observers = []
        self.size = Size(10, 30)

    def getHeight(self):
        return self.size.getHeight()

    def getWidth(self):
        return self.size.getWidth()

    def setPosition(self, position):
        self.position = position

    def setSpeed(self, speed):
        self.setSpeed = speed

    def getPosition(self):
        return self.position

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()

    def moveUp(self):
        self.position.moveUp(self.speed) 

    def moveDown(self):
        self.position.moveDown(self.speed)

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.position)
    
    def outOfBounds(self):
        pass