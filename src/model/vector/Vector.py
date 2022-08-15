from random import randint


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add(self, otherVector):
        newVector = Vector2(self.x, self.y)
        newVector.x = newVector.x + otherVector.x
        newVector.y = newVector.y + otherVector.y

        return newVector

    def substract(self, otherVector):
        newVector = Vector2(self.x, self.y)
        newVector.x = newVector.x - otherVector.x
        newVector.y = newVector.y - otherVector.y

        return newVector

    def multiply(self, value):
        newVector = Vector2(self.x, self.y)
        newVector.x = newVector.x * value
        newVector.y = newVector.y * value

        return newVector

    def reflectX(self):
        newVector = Vector2(self.x, self.y)
        newVector.y = - newVector.y 

        return newVector

    def reflectY(self):
        newVector = Vector2(self.x, self.y)
        newVector.x = - newVector.x
        
        return newVector

    @staticmethod
    def randomVectorNoAxis():
        randomX = randint(-1, 1)
        randomY = randint(-1, 1)

        return Vector2(randomX, randomY)

    def normalize(self):
        newVector = Vector2(self.x, self.y)

        norm = newVector.x * newVector.x + newVector.y * newVector.y

        return newVector.multiply(1 / norm)

    def get(self):
        return (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __eq__(self, vector: object) -> bool:
        if (type(vector) is not self.__class__):
            return False

        if (self.x == vector.x and self.y == vector.y):
            return True
        
        return False

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    