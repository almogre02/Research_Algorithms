import unittest


class Q2TestCase(unittest.TestCase):
    def print_sorted(self):
        test1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
        self.assertEqual(test1,{'a': 5, 'b': [10, 3, 4], 'c': [0, 3, 4, 2, 1, {8, 2, 3, 4}, 3, 9, 1], 'd': {1, 2, 3, 5, 6, 7}})
        test2 = {"a": 5, "c": 6, "b": [3, 4, 1, 2]}
        self.assertEqual(test2,{'a': 5, 'b': [10, 3, 4], 'c': [0, 3, 4, 2, 1, {8, 2, 3, 4}, 3, 9, 1], 'd': {1, 2, 3, 5, 6, 7}})
        test3 = {"a": (5,4,3), "c": 6, "b": [1, 3, 2, 4], 'd': {1, 2, 3, 5, 6, 7}}
        self.assertEqual(test3, {'a': (3,4,5), 'b': [1, 2, 3,4], 'c': [0, 1, 2, 3, 4, {8, 2, 3, 4}, 1, 3, 9],'d': {1, 2, 3, 5, 6, 7}})
        test4 = {"a": {5,4,3}, "c": 6, "b": [3, 4, 1, 2]}
        self.assertEqual(test4, {'a': {3,4,5}, 'b': [1, 2, 3,4], 'c': [0, 1, 2, 3, 4, {8, 2, 3, 4}, 1, 3, 9]})
        test5 = {"a": [2,1,(5,4,3)], "c": 6, "b": [1, 3, 2, 4]}
        self.assertEqual(test5, {'a': [1,2,(3,4,5)], 'b': [10, 3, 4], 'c': [0, 3, 4, 2, 1, {8, 2, 3, 4}, 3, 9, 1],'d': {1, 2, 3, 5, 6, 7}})
        test6 = {"d": 5, "c": ["d","c","b","a"]}
        self.assertEqual(test6, {'c':["a","b","c","d"],'d': 5})



if __name__ == '__main__':
    unittest.main()
