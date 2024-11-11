import pygame

from utils.PathManager import PathManager

class Slider:
    def __init__(self, sliderName, callback) -> None:
        self.sliderName = sliderName
        self.value = 0.5
        self.size = (150, 50)
        self.position = (50, 50)
        self.ringColor = (0,0,0) 
        self.sliderColor = (200, 200, 200)
        self.dragging = False
        self.callback = callback
        self.font = pygame.font.Font(PathManager.loadFont("outline"), 15)
        self.container = self.loadContainer()

    def loadContainer(self):
        img = pygame.image.load(PathManager.loadButton("container"))
        img = pygame.transform.scale(img, self.size)
        return img

    def setValue(self, newValue):
        self.value = newValue

    def setPosition(self, position : tuple):
        self.position = position

    def draw(self, screen):
        # Slider
        
        inputRect = pygame.Rect(self.position[0] + 6, self.position[1], self.value * self.size[0] - 11, self.size[1])
        pygame.draw.rect(screen, self.sliderColor, inputRect)

        screen.blit(self.container, self.position)

        text = self.font.render(self.sliderName, False, (0,0,0))

        screen.blit(text, 
                    (self.position[0] + self.size[0]/ 2 - (text.get_width() / 2),
                     self.position[1] + self.size[1]/ 2 - (text.get_height() / 2))
                    )

        # Ring
        # rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        # pygame.draw.rect(screen, self.ringColor, rect, 10, 4)
        # screen.blit(self.container, self.position)

    def listen(self, events, keyPressed):
        mousePos = pygame.mouse.get_pos()

        if self.isMouseOverButton(mousePos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragging = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                    self.callback("volume", self.value)
                    pygame.mixer.music.set_volume(self.value)
                
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        self.setValue((mousePos[0] - self.position[0]) / self.size[0])

            self.sliderColor = (255, 255, 255)
        else:
            self.sliderColor = (200, 200, 200)
  

    def isMouseOverButton(self, mousePos):
        if mousePos[0] >= self.position[0] and mousePos[0] <= self.position[0] + self.size[0]:
            if mousePos[1] >= self.position[1] and mousePos[1] <= self.position[1] + self.size[1]:
                return True
        return False


    