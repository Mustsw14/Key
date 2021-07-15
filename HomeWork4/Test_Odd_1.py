import unittest
from Odd import Odd

class Odd_Number(unittest.TestCase):
    def test_odd_number(self):
        return_result = []
        expected_result = [7,9,11,13]
        for result in Odd([6,7,8,9,10,11,12,13]):
            return_result.append(result)
        self.assertEqual(expected_result,return_result)