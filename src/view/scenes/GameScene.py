import pygame

from src.controller.KeyboardController import KeyboardController
from src.controller.SecondPlayerController import SecondPlayerController
from src.controller.PlayerController import PlayerController
from src.model.game.Game import Game
from src.utils.PathManager import PathManager
from src.view.scenes.GoalScene import GoalScene
from src.view.scenes.WinnerScene import WinnerScene
from src.view.views.ScoreView import ScoreView
from src.view.views.BallView import BallView
from src.view.views.PlayerView import PlayerView
from src.view.scenes.Scene import Scene

class GameScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.playersViews = []
        self.ballView = None
        self.scoreView = None
        self.views = []
        self.controllers = []
        self.game = None

        self.gameSound = pygame.mixer.Sound(PathManager.loadSound("match"))
        # self.gameBackground = self.loadBackground()
   
        self.gameSound.play()
        self.gameSound.set_volume(0.2)
        self.setup()

    def loadBackground(self):
        img = pygame.image.load(PathManager.loadBackground("match-background"))
        return pygame.transform.scale(img, (600, 600))

    def processInput(self, events, keyPressed):
        keyboardController = KeyboardController(self.app)

        keyboardController.handle(events)

        for controller in self.controllers:
            controller.handle(events)

    def update(self):
        self.game.update()
        self.app.update()

    def render(self, screen):

        if not self.game.detectWinner():
            if not self.game.detectScore():
                # screen.blit(self.gameBackground, (0,0))
                self.app.fill((0,0,0))

                for player in self.playersViews:
                    player.draw(screen)

                self.ballView.draw(screen)
            else:
                self.app.saveCurrentScene()
                self.app.changeScene(GoalScene(self.app))
        else:
            self.app.changeScene(WinnerScene(self.app, self.game.detectWinner()))

    def setup(self):
        self.game = Game()
        self.game.initialize()

        playerOne = self.game.getPlayer(0)
        playerTwo = self.game.getPlayer(1)
        ball = self.game.getBall()
        score = self.game.getScoreManager()

        playerOneController = PlayerController(playerOne)
        playerTwoController = SecondPlayerController(playerTwo)

        self.controllers.append(playerOneController)
        self.controllers.append(playerTwoController)

        playerOneView = PlayerView(playerOne, playerOneController)
        playerTwoView = PlayerView(playerTwo, playerTwoController)
        ballView = BallView(ball)
        scoreView = ScoreView(score.getScoreList())

        playerOne.addObserver(playerOneView)
        playerTwo.addObserver(playerTwoView)
        ball.addObserver(ballView)
        score.addObserver(scoreView)

        self.addPlayerView(playerTwoView)
        self.addPlayerView(playerOneView)
        self.addBallView(ballView)
        self.addScoreView(scoreView)

    def addPlayerView(self, playerView):
        self.playersViews.append(playerView)
        self.views.append(playerView)

    def addBallView(self, ballView):
        self.ballView = ballView
        self.views.append(ballView)

    def addScoreView(self, scoreView):
        self.playersViews.append(scoreView)
        self.views.append(scoreView)
