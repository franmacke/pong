import unittest

from src.model.player.Player import Player
from src.model.modifier.SizeModifier import SizeModifier
from src.model.size.Size import Size

class TestSpeedModifier(unittest.TestCase):
    def test_applyFasterModifier(self):
        # Player starts with 30 widht
        modifier = SizeModifier(1.5)
        player = Player()
        player.size = Size(2,2)

        modifier.applyModifier(player)

        self.assertEqual(player.getHeight(), 3)


        