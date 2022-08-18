import pygame
from src.utils.PathManager import PathManager
from src.view.scenes.Scene import Scene
from src.view.scenes.MainMenuScene import MainMenuScene

class WinnerScene(Scene):
    def __init__(self, app, winner) -> None:
        self.app = app
        self.winner = winner

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))

        font = pygame.font.Font(PathManager.loadFont("outline"), 30)

        winnerText = font.render(f"{self.winner} won! ", False, (255,255,255))
       

        screen.blit(winnerText, (200, 300))

    def processInput(self, events, keyPressed):
        for event in events:
            if (event.type == pygame.KEYDOWN):
                self.app.changeScene(MainMenuScene(self.app))
                pygame.mixer.stop()
