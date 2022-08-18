import pygame
from src.utils.PathManager import PathManager

class Button:
    def __init__(self, buttonName, callback) -> None:
        self.position = (10, 10)
        self.size = (150, 50)       # width, height
        self.imgNormal = self.setNormalState(buttonName)
        self.imgHover = self.setHoverState(buttonName)
        self.imgPressed = self.setPressedState(buttonName)
        self.state = self.imgNormal
        self.callback = callback
        self.hoverSound = pygame.mixer.Sound(PathManager.loadSound("hover"))
        self.hovered = False

    def setNormalState(self, img):
        img = pygame.image.load(PathManager.loadButton(f"{img}-normal"))
        img = pygame.transform.scale(img, self.size)
        return img

    def setHoverState(self, img):
        img = pygame.image.load(PathManager.loadButton(f"{img}-hover"))
        img = pygame.transform.scale(img, self.size)
        return  img
        
    def setPressedState(self, img):
        img = pygame.image.load(PathManager.loadButton(f"{img}-pressed"))
        img = pygame.transform.scale(img, self.size)
        return img
    
    def setPosition(self, position : tuple):
        self.position = position

    def setSize(self, size : tuple):
        self.size = size
        
    def setCallback(self, callback):
        self.callback = callback

    def onClick(self):
        self.callback()

    def draw(self, screen):
        screen.blit(self.state, self.position)

    def listen(self, events, keyPressed):
        mousePos = pygame.mouse.get_pos()

        if (self.isMouseOverButton(mousePos)):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = self.imgPressed
                if event.type == pygame.MOUSEBUTTONUP:
                    self.onClick()
            self.state = self.imgHover
            if not self.hovered:
                self.hoverSound.play()
                self.hovered = True
        else:
            self.hovered = False
            self.state = self.imgNormal    
                
    def isMouseOverButton(self, mousePos):
        if mousePos[0] >= self.position[0] and mousePos[0] <= self.position[0] + self.size[0]:
            if mousePos[1] >= self.position[1] and mousePos[1] <= self.position[1] + self.size[1]:
                return True
        return False

