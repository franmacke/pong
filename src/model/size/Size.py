from model.vector.Vector import Vector2

class Size:
    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCenter(self):
        return Vector2(self.width / 2, self.height / 2)

    def changeSize(self, value):
        self.height = self.height * value
    
