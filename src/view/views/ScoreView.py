import pygame

from model.observer.Observer import Observer
from view.views.Drawable import Drawable
from utils.PathManager import PathManager

class ScoreView(Observer, Drawable):
    def __init__(self, scoreManager) -> None:
        self.score = scoreManager

    def draw(self, screen):
        font = pygame.font.Font(PathManager.loadFont("outline"), 20)

        leftSideScore = font.render("Player 1", False, (255,255,255))
        rightSideScore = font.render("Player 2", False, (255,255,255))

        firstScore = font.render(str(self.score.get(1)), False, (255,255,255))
        secondScore = font.render(str(self.score.get(2)), False, (255,255,255))

        screen.blit(leftSideScore, (10,10))
        screen.blit(rightSideScore, (430,10))

        screen.blit(firstScore, (10,50))
        screen.blit(secondScore, (570,50))



    def update(self, score):
        self.score = score