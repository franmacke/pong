import pygame

from src.model.observer.Observer import Observer
from src.view.views.Drawable import Drawable

class PlayerView(Observer, Drawable):
    def __init__(self, player, controller) -> None:
        self.playerController = controller
        self.position = player.getPosition()
        self.size = player.getSize()

    def draw(self, screen):
        rect = pygame.Rect(self.position.getX(), self.position.getY(), self.size.getWidth(), self.size.getHeight())
        pygame.draw.rect(screen, (255,255,255), rect)

    def update(self, object):
        self.position = object.getPosition()
        self.size = object.getSize()