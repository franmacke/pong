import pygame

class SecondPlayerController:
    def __init__(self, player) -> None:
        self.player = player

    def handle(self, events):
        for event in events:
            if (event.type == pygame.QUIT):
                pygame.quit()

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    self.player.moveUp()

                if (event.key == pygame.K_DOWN):
                    self.player.moveDown()

                self.player.notifyObservers()