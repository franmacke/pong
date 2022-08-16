
from tkinter.messagebox import RETRY
from src.model import score
from src.model.player.Player import Player
from src.model.ball.Ball import Ball
from src.model.position.Position import Position
from src.model.score.Score import Score

class Game:
    def __init__(self) -> None:
        self.players = []
        self.ball = None
        self.scoreManager = None
        self.gameObjects = []
        self.maxWidth = 600
        self.maxHeight = 600

    def resetPosition(self):
        playerOne = self.getPlayer(1)
        playerOne.setPosition(Position(0, 300))
        
        playerTwo = self.getPlayer(2)
        playerTwo.setPosition(Position(590, 300))

        self.ball.setPosition(Position(300, 300))

        for object in self.gameObjects:
            object.notifyObservers()

    def initialize(self):
        playerOne = Player()
        playerOne.setPosition(Position(0, 300))
        playerOne.setId(1)
        self.addPlayer(playerOne)

        playerTwo = Player()
        playerTwo.setPosition(Position(590, 300))
        playerTwo.setId(2)
        self.addPlayer(playerTwo)

        ball = Ball()
        ball.setPosition(Position(300, 300))
        self.addBall(ball)

        score = Score(self.players)
        self.addScoreManager(score)

    def update(self):
        self.ball.move()
        self.detectBallCollisions()
        self.detectMaxScreenCollision()
        self.detectScore()

    def getPlayers(self):
        return self.players

    def getPlayer(self, number):
        return self.players[number - 1]

    def getBall(self):
        return self.ball

    def getScoreManager(self):
        return self.scoreManager

    def addPlayer(self, player):
        self.players.append(player)
        self.addGameObject(player)

    def addBall(self, ball):
        self.ball = ball
        self.addGameObject(ball)

    def addScoreManager(self, scoreManager):
        self.scoreManager = scoreManager

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
        if self.ball.getX() < 0:
            self.resetPosition()
            print("Punto para jugador 2")
            self.scoreManager.score(self.getPlayer(2))

        if self.ball.getX() > self.maxWidth:
            self.resetPosition()
            print("Punto para jugador 1")
            self.scoreManager.score(self.getPlayer(1))