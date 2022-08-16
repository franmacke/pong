from src.controller.KeyboardController import KeyboardController
from src.controller.SecondPlayerController import SecondPlayerController
from src.controller.PlayerController import PlayerController
from src.model.game.Game import Game
from src.view.views.BallView import BallView
from src.view.views.PlayerView import PlayerView
from src.view.scenes.Scene import Scene

class GameScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.playersViews = []
        self.ballView = None
        self.views = []
        self.controllers = []
        self.game = None

        self.setup()

    def processInput(self, events, keyPressed):
        keyboardController = KeyboardController(self.app)

        keyboardController.handle(events)

        for controller in self.controllers:
            controller.handle(events)

    def update(self):
        self.game.update()
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))

        for player in self.playersViews:
            player.draw(screen)

        self.ballView.draw(screen)

    def setup(self):
        self.game = Game()
        self.game.initialize()

        playerOne = self.game.getPlayer(0)
        playerTwo = self.game.getPlayer(1)
        ball = self.game.getBall()

        playerOneController = PlayerController(playerOne)
        playerTwoController = SecondPlayerController(playerTwo)

        self.controllers.append(playerOneController)
        self.controllers.append(playerTwoController)

        playerOneView = PlayerView(playerOne.getPosition(), playerOneController)
        playerTwoView = PlayerView(playerTwo.getPosition(), playerTwoController)
        ballView = BallView(ball.getPosition())

        playerOne.addObserver(playerOneView)
        playerTwo.addObserver(playerTwoView)
        ball.addObserver(ballView)

        self.addPlayerView(playerTwoView)
        self.addPlayerView(playerOneView)
        self.addBallView(ballView)
    
    def addPlayerView(self, playerView):
        self.playersViews.append(playerView)
        self.views.append(playerView)

    def addBallView(self, ballView):
        self.ballView = ballView
        self.views.append(ballView)