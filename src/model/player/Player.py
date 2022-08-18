
from src.model.collider.BoxCollider import BoxCollider
from src.model.collider.Collider import Collider
from src.model.observer.Observable import Observable
from src.model.position.Position import Position
from src.model.positionable.Positionable import Positionable
from src.model.sizable.Sizable import Sizable
from src.model.size.Size import Size

class Player(Positionable, Observable, Sizable, Collider):
    def __init__(self) -> None:
        self.id = None
        self.speed = 15
        self.position = Position(0,0)
        self.observers = []
        self.size = Size(10, 100)
        self.score = 1
        self.collider = Collider(self)

    def outOfBounds(self):
        pass

    def reset(self):
        self.position = Position(0,0)
        self.collider = Collider(self)

    def horizontalBounce(self):
        pass

    def verticalBounce(self):
        pass

    def onCollision(self, objectCollided):
        self.collider.reactToCollision(objectCollided)

    def scoreGoal(self):
        return self.score

    def changeSpeed(self, value):
        self.speed = self.speed * value

    def changeSize(self, value):
        self.size.changeSize(value)

    def getHeight(self):
        return self.size.getHeight()

    def getWidth(self):
        return self.size.getWidth()

    def getCenter(self):
        return self.position.get().add(self.size.getCenter())

    def setPosition(self, position):
        self.position = position

    def setId(self, id):
        self.id = id

    def setSpeed(self, speed):
        self.speed = speed

    def getSize(self):
        return self.size

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
            observer.update(self)

    