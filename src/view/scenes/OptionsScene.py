import thorpy
from src.view.scenes.PauseScene import PauseScene

from src.view.scenes.Scene import Scene

class OptionScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.menu = None

    def update(self):
        pass

    def render(self, screen):
        self.app.fill((0,0,0))

        backButton = thorpy.make_button("Volver", func=lambda: self.backToPauseScene())
        quitButton = thorpy.make_button("Salir", func=thorpy.functions.quit_func)

        background = thorpy.Background(
            color=(220,220,200),
            elements=[backButton, quitButton]
        )

        thorpy.store(background)

        self.menu = thorpy.Menu(background)
        self.menu.play()

    def processInput(self, events, keyPressed):
        pass

    def backToPauseScene(self):
        self.menu.set_leave()
        self.app.changeScene(PauseScene(self.app))