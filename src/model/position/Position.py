from src.model.vector.Vector import Vector2

class Position:
    def __init__(self, x, y) -> None:
        self.position = Vector2(x, y)
        self.unit = 1

    def moveUp(self, speed):
        self.position = self.position.add(Vector2(0, - 1 * speed))

    def moveDown(self, speed):
        self.position = self.position.add(Vector2(0, 1 * speed))

    def move(self, direction):
        self.position = self.position.add(direction)

    def get(self):
        return self.position.get()

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()

    def __str__(self) -> str:
        return f"({self.position.getX()}, {self.position.getY()})"

    def __eq__(self, position: object) -> bool:
        if (type(position) is not self.__class__):
            return False

        if (self.position == position.position):
            return True

        return False