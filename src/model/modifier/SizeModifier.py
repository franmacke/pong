from src.model.modifier.Modifier import Modifier

class SizeModifier(Modifier):
    def __init__(self, value) -> None:
        self.value = value
    
    def applyModifier(self, player):
        player.changeSize(self.value)
