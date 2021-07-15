import unittest
from Generator1 import  fibonacci

class Number_Fib(unittest.TestCase):
    def test_fib(self):
        return1_result = []
        expected1_result = [1,1,2,3,5,8,13,21,34]

        it = fibonacci()
        for i in range(9):
            return1_result.append(next(it))

        self.assertEqual(expected1_result,return1_result)