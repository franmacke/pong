import thorpy

from src.view.Drawable import Drawable

class MenuView(Drawable):
    def __init__(self) -> None:
        pass

    def draw(self):
        playButton = thorpy.make_button("Jugar")
        quitButton = thorpy.make_button("Salir", func=thorpy.functions.quit_func)

        background = thorpy.Background(
            color=(220,220,200),
            elements=[playButton, quitButton]
        )

        thorpy.store(background)

        menu = thorpy.Menu(background)
        menu.play()


