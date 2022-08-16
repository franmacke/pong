import thorpy, pygame

from src.view.scenes.Scene import Scene
from src.view.scenes.GameScene import GameScene

class MainMenuScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app
        self.menu = None

    def update(self):
        self.app.update()

    def render(self, screen):
        self.app.fill((0,0,0))

        playButton = thorpy.make_button("Jugar", func=lambda: self.setNextScene(GameScene(self.app)))
        quitButton = thorpy.make_button("Salir", func=thorpy.functions.quit_func)

        background = thorpy.Background(
            color=(220,220,200),
            elements=[playButton, quitButton]
        )

        thorpy.store(background)

        self.menu = thorpy.Menu(background)
        self.menu.play()
        
    def processInput(self, events, keyPressed):
        pass

    def setNextScene(self, scene):
        self.menu.set_leave()
        self.app.changeScene(scene)

    