import pygame

from src.settings.Settings import Settings

from .view.scenes.GameScene import GameScene
from src.view.scenes.MultiplayerScene import MultiplayerScene
from src.view.scenes.MainMenuScene import MainMenuScene
from src.view.scenes.PauseScene import PauseScene
from src.view.scenes.OptionsScene import OptionScene


class Application:
    def __init__(self) -> None:
        self.running = True
        self.scene = None
        self.saveScene = None
        self.display = None
        self.clock = pygame.time.Clock()
        self.mainMenu = None
        self.settings = Settings()
        self.mixers = []

    def initalize(self):

        pygame.init()
        pygame.display.set_caption('P O N G')
        pygame.font.init()
        pygame.mixer.init()

        self.display = pygame.display.set_mode((600,600))

    def run(self):
        self.initalize()

        self.mainMenu = MainMenuScene(self)

        self.changeScene(self.mainMenu)

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
        self.changeScene(optionScene)
    
    def restart(self):
        self.changeScene(GameScene(self))

    def saveCurrentScene(self):
        self.saveScene = self.scene
    
    def loadSavedScene(self):
        self.scene = self.saveScene

    def goToMainMenu(self):
        self.changeScene(self.mainMenu)

    def play(self):
        self.changeScene(self.saveScene)

    def playMultiplayer(self):
        self.changeScene(MultiplayerScene(self))

    def getSetting(self, settingName):
        return self.settings.getSetting(settingName)

    def setSetting(self, key, value):
        self.settings.setSetting(key, value)

    def quit(self):
        self.running = False
        pygame.font.quit()
        pygame.mixer.quit()
        pygame.quit()

    def fill(self, backgroud):
        self.display.fill(backgroud)

    def update(self):
        pygame.display.update()

    def addMixer(self, mixer):
        self.mixers.append(mixer)