import pygame
from src.view.components.Button import Button

from src.utils.Color import Color

from src.view.scenes.Scene import Scene
from src.utils.PathManager import PathManager

class MainMenuScene(Scene):
    def __init__(self, app) -> None:
        self.app = app
        self.mixer = pygame.mixer.Sound(PathManager.loadSound("intro"))
        self.font = pygame.font.Font(PathManager.loadFont("outline"), 50)
        self.buttons = []
        
        self.setup()

    def setup(self):
        self.loadMusic()

        playButton = Button("Play", self.startNewGame, (111, 232, 144))
        playButton.setPosition((230, 300))

        muliplayerButton = Button("Multi", self.startMultiGame, (181, 102, 227))
        muliplayerButton.setPosition((230, 360))

        optionButton = Button("Settings", self.app.options, (43, 138, 240))
        optionButton.setPosition((230, 420))

        quitButton = Button("Exit", self.quit, (242, 73, 115))
        quitButton.setPosition((230, 480))

        self.buttons.append(playButton)
        self.buttons.append(muliplayerButton)
        self.buttons.append(optionButton)
        self.buttons.append(quitButton)

    def loadMusic(self):
        self.mixer.play()
        self.mixer.set_volume(self.app.getSetting('volume'))

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)

        title = self.font.render("P O N G !", True, (255,255,255))
        
        for button in self.buttons:
            button.draw(screen)

        screen.blit(title, (100, 50))
        
    def processInput(self, events, keyPressed):
        for button in self.buttons:
            button.listen(events, keyPressed)

        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
        
    def startNewGame(self):
        self.pauseMusicOnLeave()
        self.app.startNewGame()

    def startMultiGame(self):
        self.pauseMusicOnLeave()
        self.app.playMultiplayer()

    def quit(self):
        self.app.quit()
    
    def pauseMusicOnLeave(self):
        self.mixer.fadeout(5)
    
    