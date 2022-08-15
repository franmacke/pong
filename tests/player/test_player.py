import unittest

from src.model.player.Player import Player
from src.model.position.Position import Position

class TestPlayer(unittest.TestCase):
    def test_movePlayerUpwards(self):
        player = Player()
        player.setPosition(Position(0, 0))
        player.setSpeed(10)

        assertPosition = Position(0, -10)

        player.moveUp()
        
        self.assertEqual(player.getPosition(), assertPosition)

    def test_movePlayerDownwards(self):
        player = Player()
        player.setPosition(Position(0, 0))
        player.setSpeed(10)

        assertPosition = Position(0, 10)

        player.moveDown()
        
        self.assertEqual(player.getPosition(), assertPosition)

    def test_movePlayerTwoTimesUpwards(self):
        player = Player()
        player.setPosition(Position(0, 0))
        player.setSpeed(10)

        assertPosition = Position(0, -20)

        player.moveUp()
        player.moveUp()
        
        self.assertEqual(player.getPosition(), assertPosition)

