import unittest
from Ex2 import Q3

class ListTestCase(unittest.TestCase):
    def test_List(self): # __getitem__ & __setitem__
        test_list= Q3.List([
        [[1,2,3,4],[5,6,7,8]],
        [[5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20],[21, 22, 23, 24]],
        ]
        )
        #__getitem__
        self.assertEqual(test_list[0, 1, 3],8)
        self.assertEqual(test_list[1, 0, 0], 5)
        self.assertEqual(test_list[2, 2, 2], 23)
        self.assertEqual(test_list[2], [[13, 14, 15, 16], [17, 18, 19, 20],[21, 22, 23, 24]]) # like regular list
        self.assertEqual(test_list[0], [[1, 2, 3, 4], [5, 6, 7, 8]]) # before append
        #test that the other functions didn't damage
        test_list[0].append(["a","b","c","d"]) # like regular list
        self.assertEqual(test_list[0, 2, 3], "d")
        self.assertEqual(test_list[0], [[1,2,3,4],[5,6,7,8],["a","b","c","d"]]) # after append
        # __setitem__
        self.assertEqual(test_list[0, 1, 3], 8)
        test_list[0,1,3]=888
        self.assertEqual(test_list[0, 1, 3], 888)
        self.assertEqual(test_list[1], [[5, 6, 7, 8], [9, 10, 11, 12]])
        test_list[1] = [8, 7, 6, 5]
        self.assertEqual(test_list[1], [8, 7, 6, 5])
        test_list[0, 2, 3]="Research Algorithms"
        self.assertEqual(test_list[0, 2, 3],"Research Algorithms")
        upper_check=test_list[0,2,3].upper() #checks that the upper() func didn't change
        self.assertEqual(upper_check, "RESEARCH ALGORITHMS")



if __name__ == '__main__':
    unittest.main()
