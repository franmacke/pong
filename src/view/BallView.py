import pygame
from src.model.observer.Observer import Observer
from src.view.Drawable import Drawable

class BallView(Observer, Drawable):
    def __init__(self, position) -> None:
        self.position = position

    def draw(self, screen):
        circle = pygame.draw.circle(screen, (0,0,0), self.position.get(), 10)

    def update(self, newPosition):
        self.position = newPosition