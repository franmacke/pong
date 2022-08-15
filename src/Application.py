import pygame, thorpy

from src.controller.KeyboardController import KeyboardController
from src.model.ball.Ball import Ball
from src.model.game.Game import Game
from src.model.player.Player import Player
from src.model.position.Position import Position
from src.view.BallView import BallView
from src.view.GameView import GameView
from src.view.MenuView import MenuView
from src.view.PlayerView import PlayerView
from src.controller.PlayerController import PlayerController
from src.controller.SecondPlayerController import SecondPlayerController


pygame.init()

DISPLAY = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()

class Application:
    def __init__(self) -> None:
        self.running = True
        self.display = None
        self.game = None
        self.controllers = []
        self.gameView = None

    def initalize(self):
        pygame.init()
        self.display = pygame.display.set_mode((600,600))

    def run(self):
        # self.initalize()
        self.startGame()

        keyboardController = KeyboardController(self)

        while self.running:
            CLOCK.tick(60)
            events = pygame.event.get()

            keyboardController.handle(events)

            for controller in self.controllers:
                controller.handle(events)

            DISPLAY.fill((255,255,255))
            self.game.startGame()
            self.gameView.draw(DISPLAY)
            self.update()

    def showMainMenu(self):
        menuView = MenuView()
        menuView.draw()

    def startGame(self):
        self.game = Game()
        gameView = GameView()

        playerOne = Player()
        playerOne.setPosition(Position(0, 300))

        playerTwo = Player()
        playerTwo.setPosition(Position(590, 300))

        ball = Ball()
        ball.setPosition(Position(300, 300))

        self.game.addPlayer(playerOne)
        self.game.addPlayer(playerTwo)
        self.game.addBall(ball)

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

        gameView.addPlayerView(playerTwoView)
        gameView.addPlayerView(playerOneView)
        gameView.addBallView(ballView)

        self.gameView = gameView

    
    def quit(self):
        self.running = False
        self.display.quit()

    def update(self):
        # pygame.display.flip()
        pygame.display.update()