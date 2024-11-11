
import pygame
from utils.Color import Color

from utils.PathManager import PathManager
from view.scenes.MainMenuScene import MainMenuScene
from view.scenes.Scene import Scene
from multiplayer.Network import Network
from view.views.MultiPlayerView import MultiPlayerView
from view.views.BallView import BallView
from controller.PlayerController import PlayerController
from view.views.ScoreView import ScoreView

DATA_PLAYER = 0
DATA_PLAYER_OPPONENT = 1
DATA_BALL = 2
DATA_SCORE = 3
MATCH_END = -1

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
        self.gameMusic = pygame.mixer.Sound(PathManager.loadSound("match"))

        self.setup()

    def setup(self):    
        firstData = self.network.getConnection()

        if firstData:
            self.playerOne = firstData[DATA_PLAYER]
            self.playerTwo = firstData[DATA_PLAYER_OPPONENT]
            self.ball = firstData[DATA_BALL]
            self.score = firstData[DATA_SCORE]

            self.generatePlayerView(self.playerOne)
            self.generatePlayerView(self.playerTwo)
            self.generateBallView(self.ball)
            self.generateScoreView(self.score)

            self.loadMusic()
          
        else:
            self.serverUnavailable()

    def loadMusic(self):
        self.gameMusic.play()
        self.gameMusic.set_volume(self.app.getSetting("volume"))
        
    def requestData(self):
        data = self.network.send(self.playerOne)
        return data

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)
    
        data = self.requestData()

        if not data:
            print(data)
            print("Server unavailable")
            self.app.changeScene(MainMenuScene(self.app))
    
        else:
            self.updateView(self.playerOne, data[DATA_PLAYER])
            self.updateView(self.playerTwo, data[DATA_PLAYER_OPPONENT])
            self.updateView(self.ball, data[DATA_BALL])
            self.updateScoreView(data[DATA_SCORE])

            for view in self.views:
                view.draw(screen)

    def processInput(self, events, keyPressed):
        playerController = PlayerController(self.playerOne)
        playerController.handle(events)

        data = self.requestData()
        
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

    def serverUnavailable(self):
        self.app.goToMainMenu()