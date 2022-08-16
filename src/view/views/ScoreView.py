import pygame

from src.model.observer.Observer import Observer
from src.view.views.Drawable import Drawable
from src.utils.PathManager import PathManager

class ScoreView(Observer, Drawable):
    def __init__(self, scoreManager) -> None:
        self.score = scoreManager

    def draw(self, screen):
        font = pygame.font.Font(PathManager.loadFont("outline"), 30)

        leftSideScore = font.render("Player 1", False, (255,255,255))
        rightSideScore = font.render("Player 2", False, (255,255,255))

        firstScore = font.render(str(self.score.get(1)), False, (255,255,255))
        secondScore = font.render(str(self.score.get(2)), False, (255,255,255))

        screen.blit(leftSideScore, (10,30))
        screen.blit(rightSideScore, (350,30))

        screen.blit(firstScore, (150,70))
        screen.blit(secondScore, (450,70))

    def update(self, score):
        self.scoreManager = score