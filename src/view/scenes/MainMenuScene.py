import pygame
from src.view.components.Button import Button

from src.view.scenes.Scene import Scene
from src.utils.PathManager import PathManager

class MainMenuScene(Scene):
    def __init__(self, app) -> None:
        self.app = app
        self.mixer = pygame.mixer.Sound(PathManager.loadSound("intro"))
        self.font = pygame.font.Font(PathManager.loadFont("outline"), 50)
        self.buttons = []

        
        self.mixer.play()
        self.mixer.set_volume(0.2)
        self.setup()

    def setup(self):
        playButton = Button("play", self.startNewGame)
        playButton.setPosition((230, 300))

        muliplayerButton = Button("multi", self.startMultiGame)
        muliplayerButton.setPosition((230, 350))

        optionButton = Button("option", self.app.options)
        optionButton.setPosition((230, 400))

        quitButton = Button("quit", self.quit)
        quitButton.setPosition((230, 450))

        self.buttons.append(playButton)
        self.buttons.append(muliplayerButton)
        self.buttons.append(optionButton)
        self.buttons.append(quitButton)


    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))

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
    
    