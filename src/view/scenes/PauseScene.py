import thorpy

from src.view.scenes.Scene import Scene

class PauseScene(Scene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.menu = None

    def render(self, screen):
        self.app.fill((0,0,0))

        playButton = thorpy.make_button("Reanudar", func=lambda: self.play())
        optionsButton = thorpy.make_button("Opciones", func=lambda: self.options())
        quitButton = thorpy.make_button("Salir del juego", func=thorpy.functions.quit_func)

        background = thorpy.Background(
            color=(220,220,200),
            elements=[playButton, optionsButton, quitButton]
        )

        thorpy.store(background)

        self.menu = thorpy.Menu(background)
        self.menu.play()

    def options(self):
        self.menu.set_leave()
        self.app.options()

    def update(self):
        pass

    def processInput(self, events, keyPressed):
        pass

    def play(self):
        self.menu.set_leave()
        self.app.play()


