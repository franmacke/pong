from src.model.collider.BoxCollider import BoxCollider
from src.model.sizable.Sizable import Sizable
from src.model.observer.Observable import Observable
from src.model.position.Position import Position
from src.model.positionable.Positionable import Positionable
from src.model.size.Size import Size
from src.model.vector.Vector import Vector2

class Ball(Positionable, Observable, Sizable):
    def __init__(self) -> None:
        self.position = Position(0,0)
        self.direction = self.startWithRandomDirection()
        self.observers = []
        self.speed = 10
        self.size = Size(10, 10)
        self.collider = BoxCollider(self)

    def reset(self):
        self.direction = self.startWithRandomDirection()
        self.collider = BoxCollider(self)
        self.position = Position(0,0)

    def verticalBounce(self):
        self.direction = self.direction.reflectX()

    def horizontalBounce(self):
        self.direction = self.direction.reflectY()

    def onCollision(self, objectCollided):
        self.collider.onBoxCollision(objectCollided)

    def move(self):
        self.position.move(self.direction.multiply(self.speed))
        self.notifyObservers()

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position.get()

    def getHeight(self):
        return self.size.getHeight()

    def getWidth(self):
        return self.size.getWidth()

    def getCenter(self):
        return self.position.get().add(self.size.getCenter())

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()

    def startWithRandomDirection(self):
        return Vector2(-1,2).normalize().multiply(1)

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.position)

    def outOfBounds(self):
        self.verticalBounce()