import thorpy, pygame

from src.view.scenes.Scene import Scene
from src.utils.PathManager import PathManager

class MainMenuScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app
        self.menu = None

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))

        font = pygame.font.Font(PathManager.loadFont("outline"), 10)

        title = font.render("P O N G", True, (255,255,255))

        playButton = thorpy.make_button("Jugar", func=lambda: self.startNewGame())
        quitButton = thorpy.make_button("Salir", func=thorpy.functions.quit_func)

        background = thorpy.Background(
            color=(0,0,0),
            elements=[playButton, quitButton]
        )

        thorpy.store(background)

        self.menu = thorpy.Menu(background)
        self.menu.play()
        
    def processInput(self, events, keyPressed):
        pass

    def startNewGame(self):
        self.menu.set_leave()
        self.app.startNewGame()


    