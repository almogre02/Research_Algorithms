import random
import unittest
from Ex2 import Q2

@Q2.lastcall
def f(x: int):
    return x ** 2

@Q2.lastcall
def f1(x: int):
    return x * 3
class LastCallTestCase(unittest.TestCase):
    def test_lastcall(self):
        '''
        @Q2.lastcall
        def f(x: int):
            return x ** 2

        @Q2.lastcall
        def f1(x: int):
            return x * 3
        :return:
        '''


        test1=f(2)
        test2=f1(3)
        print(test1)
        print(test2)
        self.assertEqual(test1, 4)
        self.assertEqual(test2, 9)

        '''
        test_number = random.randint(0, 10000)
        print(test_number)
        self.assertEqual(f(test_number), test_number ** 2)
        self.assertEqual(f1(test_number), test_number * 3)
        '''



if __name__ == '__main__':
    unittest.main()
