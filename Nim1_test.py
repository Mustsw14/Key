import Nim1
import unittest


class Nim1test(unittest.TestCase):
    def test_is_game_over(self):
        self.assertTrue(Nim1.is_game_over([1, 0, 0]))
