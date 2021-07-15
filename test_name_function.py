import unittest
from name_function import getname


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = getname('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted1_name = getname('janis','joplin','jae')
        self.assertEqual(formatted1_name, 'Janis Jae Joplin')

    def test_max_from_2_tuples():
if __name__ == '__main__':
    unittest.main()
