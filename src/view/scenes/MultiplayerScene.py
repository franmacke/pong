
import socket
from src.view.scenes.MainMenuScene import MainMenuScene
from src.view.scenes.Scene import Scene
from src.multiplayer.Network import Network
from src.view.views.MultiPlayerView import MultiPlayerView
from src.view.views.BallView import BallView
from src.controller.PlayerController import PlayerController
from src.view.views.ScoreView import ScoreView

DATA_PLAYER = 0
DATA_PLAYER_OPPONENT = 1
DATA_BALL = 2
DATA_SCORE = 3

class MultiplayerScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.network = Network()
        self.playerOne = None
        self.playerTwo = None
        self.ball = None
        self.views = []
        self.score = None
        self.initialized = False

        self.setup()

    def setup(self):
        try:
            firstData = self.network.getConnection()

            self.playerOne = firstData[DATA_PLAYER]
            self.playerTwo = firstData[DATA_PLAYER_OPPONENT]
            self.ball = firstData[DATA_BALL]
            self.score = firstData[DATA_SCORE]

            self.generatePlayerView(self.playerOne)
            self.generatePlayerView(self.playerTwo)
            self.generateBallView(self.ball)
            self.generateScoreView(self.score)
        except socket.error as error:
            print("Server unavailable")
            self.initialized = False
            self.app.changeScene(MainMenuScene(self.app))

    def update(self):
        data = self.network.send(self.playerOne)

        self.updateView(self.playerOne, data[DATA_PLAYER])
        self.updateView(self.playerTwo, data[DATA_PLAYER_OPPONENT])
        self.updateView(self.ball, data[DATA_BALL])
        self.updateScoreView(data[DATA_SCORE])

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

    def generateScoreView(self, score):
        view = ScoreView(score.getScoreList())
        score.addObserver(view)
        self.addView(view)

    def updateView(self, object, newObject):
        object.setPosition(newObject.getPosition())
        object.notifyObservers()

    def updateScoreView(self, newScore):
        self.score.setScore(newScore.getScoreList())
        self.score.notifyObservers()

    