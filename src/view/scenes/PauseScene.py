
import pygame

from src.utils.Color import Color
from src.view.components.Button import Button
from src.view.scenes.Scene import Scene

class PauseScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.buttons = []

        self.setup()

    def setup(self):
        resumeButton = Button("Resume", self.play, Color.COLOR_GREEN)
        resumeButton.setPosition((230, 200))

        restartButton = Button("Restart", self.restart, Color.COLOR_RED)
        restartButton.setPosition((230, 260))

        optionsButton = Button("Options", self.options, Color.COLOR_BLUE)
        optionsButton.setPosition((230, 320))

        backMenuButton = Button("Main Menu", self.app.goToMainMenu, Color.COLOR_RED)
        backMenuButton.setPosition((230, 380))

        self.buttons.append(resumeButton)
        self.buttons.append(restartButton)
        self.buttons.append(optionsButton)
        self.buttons.append(backMenuButton)

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)

        for button in self.buttons:
            button.draw(screen)

    def options(self):
        self.app.options()

    def restart(self):
        self.app.restart()

    def update(self):
        self.app.update()

    def processInput(self, events, keyPressed):
        for event in events:
            if event.type == pygame.QUIT:
                self.app.quit()
        
        for input in self.buttons:
            input.listen(events, keyPressed)

    def play(self):
        self.app.play()


