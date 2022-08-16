
class Size:
    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def changeSize(self, value):
        self.height = self.height * value
    
