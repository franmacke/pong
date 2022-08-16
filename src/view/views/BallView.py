import pygame
from src.model.observer.Observer import Observer
from src.view.views.Drawable import Drawable

class BallView(Observer, Drawable):
    def __init__(self, position) -> None:
        self.position = position

    def draw(self, screen):
        rect = pygame.Rect(self.position.getX(), self.position.getY(), 10, 10)
        pygame.draw.rect(screen, (255,255,255), rect)

    def update(self, newPosition):
        self.position = newPosition