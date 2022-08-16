import pygame

from src.model.observer.Observer import Observer
from src.view.views.Drawable import Drawable

class ScoreView(Observer, Drawable):
    def __init__(self, playerScore) -> None:
        self.score = playerScore

    def draw(self, screen):
        font = pygame.font.SysFont('Arial', 30)

        text_surface = font.render(self.score, False, (0,0,0))
        screen.blit()

    def update(self, score):
        self.score = score