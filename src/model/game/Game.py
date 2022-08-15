
from src.model.player.Player import Player
from src.model.ball.Ball import Ball
from src.model.position.Position import Position

class Game:
    def __init__(self) -> None:
        self.players = []
        self.ball = None
        self.gameObjects = []
        self.maxWidth = 600
        self.maxHeight = 600

    def startGame(self):
        self.ball.move()
        self.detectBallCollisions()
        self.detectMaxScreenCollision()

    def getPlayers(self):
        return self.players

    def getBall(self):
        return self.ball

    def addPlayer(self, player):
        self.players.append(player)
        self.addGameObject(player)

    def addBall(self, ball):
        self.ball = ball
        self.addGameObject(ball)

    def addGameObject(self, object):
        self.gameObjects.append(object)

    def detectBallCollisions(self):    
        for player in self.players:
            if self.isColliding(player, self.ball):
                self.ball.oppositeBounce()


    def isColliding(self, firstObject, secondObject):
        collisionX = (
            firstObject.getX() + firstObject.getWidth() >= secondObject.getX() and
            secondObject.getX() + secondObject.getWidth() >= firstObject.getX()
        )

        collisionY = (
            firstObject.getY() + firstObject.getHeight() >= secondObject.getY() and
            secondObject.getY() + secondObject.getHeight() >= firstObject.getY()
        )

        collision = collisionX and collisionY
        return collision


    def detectMaxScreenCollision(self):
        for object in self.gameObjects:
            if object.getY() >= self.maxHeight or object.getY() <= 0:
                object.outOfBounds()

    def detectScore(self):
        pass
        # for object in self.gameObjects:
        #     if object.getY() >= self.maxWidth or object.getY() <= 0:
        #         object.score()