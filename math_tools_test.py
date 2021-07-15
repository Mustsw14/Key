import math_tools
import unittest


class MathToolTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(25,math_tools.square(5))