import pygame

class KeyboardController:
    def __init__(self, app) -> None:
        self.app = app

    def handle(self, events):
        for event in events:
            if (event.type == pygame.QUIT):
                self.app.quit()


            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.app.pause()

