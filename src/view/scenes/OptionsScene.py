import pygame
from utils.Color import Color
from utils.PathManager import PathManager
from view.components.Button import Button
from view.components.Slider import Slider
from view.scenes.PauseScene import PauseScene


from view.scenes.Scene import Scene

class OptionScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.menu = None
        self.inputs = []
        self.font = pygame.font.Font(PathManager.loadFont("outline"), 15)
        
        self.setup()

    def setup(self):
        musicSlider = Slider("Volume", self.app.setSetting)
        musicSlider.setPosition((230, 200))

        goBackButton = Button("Back", self.goBack, (52, 235, 219))
        goBackButton.setPosition((230, 260))

        self.inputs.extend([musicSlider, goBackButton])

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)

        for input in self.inputs:
            input.draw(screen)


    def processInput(self, events, keyPressed):
        for event in events:
            if event.type == pygame.QUIT:
                self.app.quit()
        
        for input in self.inputs:
            input.listen(events, keyPressed)


    def goBack(self):
        self.goToPrevScene()