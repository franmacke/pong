import pygame
from src.utils.PathManager import PathManager

class Button:
    def __init__(self, buttonName, callback, color) -> None:
        self.position = (10, 10)
        self.size = (150, 50)       # width, height
        self.buttonName = buttonName
        self.colorBackground = (color[0] - 15, color[1] - 15, color[2] - 15)
        self.state = self.colorBackground
        self.callback = callback
        self.container = self.loadContainer()
        self.hoverSound = pygame.mixer.Sound(PathManager.loadSound("hover"))
        self.font = pygame.font.Font(PathManager.loadFont("outline"), 15)
        self.hovered = False

    def loadContainer(self):
        img = pygame.image.load(PathManager.loadButton("container"))
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

        # Ring
        rect = pygame.Rect(self.position[0] + 6, self.position[1], self.size[0] - 12, self.size[1])
        pygame.draw.rect(screen, self.state, rect)

        screen.blit(self.container, self.position)

        text = self.font.render(self.buttonName, False, (0,0,0))

        screen.blit(text, 
                    (self.position[0] + self.size[0]/ 2 - (text.get_width() / 2),
                     self.position[1] + self.size[1]/ 2 - (text.get_height() / 2))
                    )

    def listen(self, events, keyPressed):
        mousePos = pygame.mouse.get_pos()
        color = self.colorBackground

        if (self.isMouseOverButton(mousePos)):
            self.state = (color[0] + 15, color[1] + 15, color[2] + 15)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONUP:
                    self.onClick()
            if not self.hovered:
                self.hoverSound.play()
                self.hovered = True
        else:
            self.hovered = False
            self.state = color   
                
    def isMouseOverButton(self, mousePos):
        if mousePos[0] >= self.position[0] and mousePos[0] <= self.position[0] + self.size[0]:
            if mousePos[1] >= self.position[1] and mousePos[1] <= self.position[1] + self.size[1]:
                return True
        return False

