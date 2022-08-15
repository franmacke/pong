import unittest
from src.model.vector.Vector import Vector2

class TestVector2(unittest.TestCase):
    def test_sumTwoVectors(self):
        vectorOne = Vector2(0, 1)
        vectorTwo = Vector2(2, 2)

        sum = Vector2(2, 3)

        self.assertEqual(vectorOne.add(vectorTwo), sum)

    def test_substractTwoVectors(self):
        vectorOne = Vector2(0, 1)
        vectorTwo = Vector2(2, 2)

        substract = Vector2(-2, -1)
        
        self.assertEqual(vectorOne.substract(vectorTwo), substract)

    def test_twoVectorsAreEqual(self):
        vectorOne = Vector2(0, 0)
        vectorTwo = Vector2(0, 0)

        self.assertEqual(vectorOne, vectorTwo)

    def test_multiplyVectorByNumber(self):
        vector = Vector2(1,0)
        value = 2
        assertVector = Vector2(2,0)

        self.assertEqual(vector.multiply(2), assertVector)