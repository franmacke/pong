
from abc import abstractmethod


class Collider:
    def __init__(self, object) -> None:
        self.object = object
        
    def checkCollision(self, objectCollided):
        if (self.object.getX() + self.object.getWidth() <= objectCollided.getX() or
            objectCollided.getX() + objectCollided.getWidth() <= self.object.getX() or
            self.object.getY() + self.object.getHeight() <= objectCollided.getY() or
            objectCollided.getY() + objectCollided.getHeight() <= self.object.getY()
        ):
            return False

        print("Collision")
        return True

    def onBoxCollision(self, objectCollided):
        if self.checkCollision(objectCollided):
            objectCollided.onCollision(self.object)

    def reactToCollision(self, objectCollided):
        leftCollision = self.object.getX() + self.object.getWidth() - objectCollided.getX()
        rightCollision = objectCollided.getX() + objectCollided.getWidth() - self.object.getX()
        topCollision = self.object.getY() + self.object.getHeight() - objectCollided.getY()
        bottomCollision = objectCollided.getY() + objectCollided.getHeight() - objectCollided.getY() 

        collisions = [leftCollision, rightCollision, topCollision, bottomCollision]

        if leftCollision == min(collisions):
            objectCollided.horizontalBounce()

        elif rightCollision == min(collisions):
            objectCollided.horizontalBounce()

        elif topCollision == min(collisions):
            objectCollided.verticalBounce()
            
        elif bottomCollision == min(collisions):
            objectCollided.verticalBounce()

        
