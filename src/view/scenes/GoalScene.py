
import pygame
from src.utils.PathManager import PathManager
from src.view.scenes.Scene import Scene

class GoalScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.animationPosition = 600
        self.animationSpeed = 5
        self.reachedTop = False

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))
        font = pygame.font.Font(PathManager.loadFont("outline"), 30)

        text = font.render("G O A L !", False, (255,255,255))
 
        if (not self.reachedTop and self.animationPosition > 300):
            self.animationPosition -= self.animationSpeed
        else:
            if (self.animationPosition > 600):
                self.onAnimationEnd()
            else:
                self.reachedTop = True
                self.animationPosition += self.animationSpeed

        screen.blit(text, (170, self.animationPosition))

    def processInput(self, events, keyPressed):
        pass

    def onAnimationEnd(self):
        self.app.loadSavedScene()