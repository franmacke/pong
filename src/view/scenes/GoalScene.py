
import pygame
from src.utils.Color import Color
from src.utils.PathManager import PathManager
from src.view.scenes.Scene import Scene

class GoalScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.animationPosition = 600
        self.animationSpeed = 5
        self.reachedTop = False
        self.goalSound = pygame.mixer.Sound(PathManager.loadSound("goal"))
        self.cheeringSound = pygame.mixer.Sound(PathManager.loadSound("cheering"))
        self.loadMusic()

    def update(self):
        self.app.update()

    def loadMusic(self):
        self.goalSound.play()
        self.goalSound.set_volume(self.app.getSetting("volume"))
        self.cheeringSound.play()
        self.cheeringSound.set_volume(self.app.getSetting("volume"))

    def render(self, screen):
        self.app.fill(Color.COLOR_BACKGROUND)
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