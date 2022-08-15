import thorpy, pygame

from src.model.observer.Observer import Observer
from src.view.Drawable import Drawable

class PlayerView(Observer, Drawable):
    def __init__(self, position, controller) -> None:
        self.playerController = controller
        self.position = position

    def draw(self, screen):
        rect = pygame.Rect(self.position.getX(), self.position.getY(), 10, 30)
        pygame.draw.rect(screen, (255,0,0), rect)

    def update(self, newPosition):
        self.position = newPosition