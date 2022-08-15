import thorpy

from src.view.Drawable import Drawable


class GameView(Drawable):
    def __init__(self) -> None:
        self.playersViews = []
        self.ballView = []

    def addPlayerView(self, playerView):
        self.playersViews.append(playerView)

    def addBallView(self, ballView):
        self.ballView = ballView

    def draw(self, screen):
        for player in self.playersViews:
            player.draw(screen)

        self.ballView.draw(screen)
