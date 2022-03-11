import unittest
from Ex1 import Q3


class Q3Test(unittest.TestCase):
    def test_find_root(self):
        print(Q3.find_root(lambda x: x**2, 2, 1))
        self.assertEqual(Q3.find_root(lambda x: x**2, 2, 1),4)


if __name__ == '__main__':
    unittest.main()
