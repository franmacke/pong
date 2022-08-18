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

        
        musicSlider = thorpy.SliderX(100, limvals=(0, 1), text="Music", initial_value=0.5, type_=float)

        backButton = thorpy.make_button("Volver", func=lambda: self.goBack())

        background = thorpy.Background(
            color=(0,0,0),
            elements=[musicSlider, backButton]
        )

        thorpy.store(background)

        self.menu = thorpy.Menu(background)
        self.menu.play()

    def processInput(self, events, keyPressed):
        pass

    def goBack(self):
        self.menu.set_leave()
        self.goToPrevScene()