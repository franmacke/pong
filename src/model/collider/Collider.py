
from abc import abstractmethod


class Collider:
    def __init__(self, object) -> None:
        self.object = object
        
    @abstractmethod
    def onBoxCollision(self, objectCollided):
        pass
