from src.model.modifier.Modifier import Modifier

class SpeedModifier(Modifier):
    def __init__(self, value) -> None:
        self.value = value

    def applyModifier(self, player):
        player.changeSpeed(self.value)
