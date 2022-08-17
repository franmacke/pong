import pygame, os
from pathlib import Path


from .view.scenes.GameScene import GameScene
from src.view.scenes.MainMenuScene import MainMenuScene
from src.view.scenes.PauseScene import PauseScene
from src.view.scenes.OptionsScene import OptionScene

class Application:
    def __init__(self) -> None:
        self.running = True
        self.scene = None
        self.saveScene = None
        self.display = pygame.display.set_mode((600,600))
        self.clock = pygame.time.Clock()

    def initalize(self):
        pygame.init()
        pygame.font.init()

    def run(self):
        self.initalize()

        mainMenu = MainMenuScene(self)

        self.changeScene(mainMenu)

        while self.running:
            self.clock.tick(60)

            events = pygame.event.get()
            keyPressed = pygame.key.get_pressed()

            self.scene.processInput(events, keyPressed)
            self.scene.render(self.display)
            self.scene.update()

    def changeScene(self, newScene):
        self.scene = newScene

    def startNewGame(self):
        self.changeScene(GameScene(self))

    def pause(self):
        self.saveCurrentScene()
        pauseScene = PauseScene(self)
        self.changeScene(pauseScene)

    def options(self):
        optionScene = OptionScene(self)
        optionScene.savePreviusScene(self.scene)
        self.changeScene(OptionScene(self))
    
    def restart(self):
        self.changeScene(GameScene(self))

    def saveCurrentScene(self):
        self.saveScene = self.scene
    
    def loadSavedScene(self):
        self.scene = self.saveScene

    def play(self):
        self.changeScene(self.saveScene)

    def quit(self):
        self.running = False

    def fill(self, backgroud):
        self.display.fill(backgroud)

    def update(self):
        pygame.display.update()