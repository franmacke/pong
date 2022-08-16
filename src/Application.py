import pygame
from src.view.scenes.MainMenuScene import MainMenuScene

class Application:
    def __init__(self) -> None:
        self.running = True
        self.scene = None
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

    def quit(self):
        self.running = False

    def fill(self, backgroud):
        self.display.fill(backgroud)

    def update(self):
        pygame.display.update()