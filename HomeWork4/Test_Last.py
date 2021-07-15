import unittest
from Last import Last

class Last_Number(unittest.TestCase):
    def test_last(self):
        return_result = []
        expected_results = [11,12,13]
        for result in Last([6,7,8,9,10,11,12,13],3):
            return_result.append(result)

        self.assertEqual(expected_results,return_result)

