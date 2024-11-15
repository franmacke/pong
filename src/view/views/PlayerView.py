import pygame

from model.observer.Observer import Observer
from utils.PathManager import PathManager
from view.views.Drawable import Drawable

class PlayerView(Observer, Drawable):
    def __init__(self, player, controller) -> None:
        self.playerController = controller
        self.position = player.getPosition()
        self.size = player.getSize()
        self.moveSound = pygame.mixer.Sound(PathManager.loadSound("player-move"))

        self.moveSound.set_volume(0.1)

    def draw(self, screen):
        rect = pygame.Rect(self.position.getX(), self.position.getY(), self.size.getWidth(), self.size.getHeight())
        pygame.draw.rect(screen, (255,255,255), rect)

    def update(self, object):
        self.position = object.getPosition()
        self.size = object.getSize()
        self.moveSound.play()

