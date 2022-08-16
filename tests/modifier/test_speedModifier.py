import unittest

from src.model.player.Player import Player
from src.model.modifier.SpeedModifier import SpeedModifier

class TestSpeedModifier(unittest.TestCase):
    def test_applyFasterModifier(self):
        modifier = SpeedModifier(1.5)
        player = Player()
        player.setSpeed(1)

        modifier.applyModifier(player)

        self.assertEqual(player.speed, 1.5)


        