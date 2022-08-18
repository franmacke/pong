
from src.model.game.Game import Game
from src.view.scenes.Scene import Scene
from src.multiplayer.Network import Network
from src.view.views.MultiPlayerView import MultiPlayerView
from src.view.views.BallView import BallView
from src.controller.PlayerController import PlayerController
from src.view.views.ScoreView import ScoreView


class MultiplayerScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.network = Network()
        self.playerOne = None
        self.playerTwo = None
        self.ball = None
        self.views = []

        self.setup()

    def setup(self):
        firstData = self.network.getConnection()
        self.playerOne = firstData[0]
        self.playerTwo = firstData[1]
        self.ball = firstData[2]

        self.generatePlayerView(self.playerOne)
        self.generatePlayerView(self.playerTwo)
        self.generateBallView(self.ball)

    def update(self):
        data = self.network.send(self.playerOne)

        self.updateView(self.playerOne, data[0])
        self.updateView(self.playerTwo, data[1])
        self.updateView(self.ball, data[2])

        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))
    
        for view in self.views:
            view.draw(screen)

    def processInput(self, events, keyPressed):
        playerController = PlayerController(self.playerOne)
        playerController.handle(events)
        
    def addView(self, view):
        self.views.append(view)

    def generatePlayerView(self, player):
        view = MultiPlayerView(player)
        player.addObserver(view)
        self.addView(view)
    
    def generateBallView(self, ball):
        view = BallView(ball)
        ball.addObserver(view)
        self.addView(view)

    def updateView(self, object, newObject):
        object.setPosition(newObject.getPosition())
        object.notifyObservers()