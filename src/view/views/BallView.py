import pygame
from model.observer.Observer import Observer
from utils.PathManager import PathManager
from view.views.Drawable import Drawable

class BallView(Observer, Drawable):
    def __init__(self, ball) -> None:
        self.ball = ball
        self.position = ball.getPosition()
        self.isColliding = ball.isColliding()
        self.collisionSound = pygame.mixer.Sound(PathManager.loadSound("ball-hit"))

    def draw(self, screen):
        rect = pygame.Rect(self.position.getX(), self.position.getY(), 10, 10)
        pygame.draw.rect(screen, (255,255,255), rect)

    def update(self, ball):
        self.position = ball.getPosition()
        self.isColliding = ball.isColliding()

        if self.isColliding:
            self.collisionSound.play()