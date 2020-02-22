import unittest
from typing import List
from problem15_2 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass

    def test_normal_00(self):
        self.assertEqual([[1, -1, 0], [2, -1, -1]], self.sol.threeSum([-1,0,1,2,-1,-4]))

    def test_normal_01(self):
        self.assertEqual([[0, 0, 0]], self.sol.threeSum([0, 0, 0]))

if __name__ == "__main__":
    unittest.main()