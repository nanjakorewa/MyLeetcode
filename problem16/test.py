import unittest
from typing import List
from problem16 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass

    def test_normal_00(self):
        self.assertEqual(2, self.sol.threeSumClosest([-1,2,1,-4], 2))

    def test_normal_01(self):
        self.assertEqual(3, self.sol.threeSumClosest([-1,2,2,100], 2))

    def test_normal_02(self):
        self.assertEqual(2, self.sol.threeSumClosest([-1,2,1,-4], 1))


if __name__ == "__main__":
    unittest.main()