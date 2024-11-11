import pygame
from utils.Color import Color
from utils.PathManager import PathManager
from view.scenes.Scene import Scene
from view.scenes.MainMenuScene import MainMenuScene

class WinnerScene(Scene):
    def __init__(self, app, winner) -> None:
        self.app = app
        self.winner = winner

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)

        font = pygame.font.Font(PathManager.loadFont("outline"), 30)

        winnerText = font.render(f"{self.winner} won! ", False, (255,255,255))
       
        screen.blit(winnerText, (200, 300))

    def processInput(self, events, keyPressed):
        for event in events:
            if (event.type == pygame.KEYDOWN):
                self.app.goToMainMenu()
                pygame.mixer.stop()
