from model.collider.Collider import Collider

class BoxCollider(Collider):
    def __init__(self, object) -> None:
        super().__init__(object)
        self.collisionQueue = []

    def checkBoxCollision(self, objectCollided):
        if (
            self.object.getX() + self.object.getWidth() <= objectCollided.getX() or
            objectCollided.getX() + objectCollided.getWidth() <= self.object.getX() or
            self.object.getY() + self.object.getHeight() <= objectCollided.getY() or
            objectCollided.getY() + objectCollided.getHeight() <= self.object.getY()
        ):
            return False
        print("Collision")
        return True

    def onBoxCollision(self, objectCollided):
        if (self.checkBoxCollision(objectCollided)) and (self.collisionQueue.count(objectCollided) == 0):
            self.collisionQueue.append(objectCollided)


            leftCollision = self.object.getX() + self.object.getWidth() - objectCollided.getX()
            rightCollision = objectCollided.getX() + objectCollided.getWidth() - self.object.getX()
            topCollosion = self.object.getY() + self.object.getHeight() - objectCollided.getY()
            bottomCollision = objectCollided.getY() + objectCollided.getHeight() - objectCollided.getY() 

            collisions = [leftCollision, rightCollision, topCollosion, bottomCollision]


            if leftCollision == min(collisions):
                objectCollided.horizontalBounce()
                self.object.horizontalBounce()

            elif rightCollision == min(collisions):
                objectCollided.horizontalBounce()
                self.object.horizontalBounce()

            elif topCollosion == min(collisions):
                objectCollided.verticalBounce()
                self.object.verticalBounce()
                
            elif bottomCollision == min(collisions):
                objectCollided.verticalBounce()
                self.object.verticalBounce()
        else:
            try:
                self.collisionQueue.remove(objectCollided)
            except:
                pass