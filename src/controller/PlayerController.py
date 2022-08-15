import pygame

class PlayerController:
    def __init__(self, player) -> None:
        self.player = player

    def handle(self, events):
        for event in events:
            # if (event.type == pygame.QUIT):
            #     pygame.quit()

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_w):
                    self.player.moveUp()

                if (event.key == pygame.K_s):
                    self.player.moveDown()

                # print(self.player.getPosition())
                self.player.notifyObservers()