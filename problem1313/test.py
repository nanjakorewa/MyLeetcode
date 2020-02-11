import unittest
from problem1313 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass

    def test_normal_00(self):
        self.assertEqual([2,4,4,4,6,6,6,6,6], self.sol.decompressRLElist([1,2,3,4,5,6]))

    def test_normal_01(self):
        self.assertEqual([2], self.sol.decompressRLElist([1,2]))

if __name__ == "__main__":
    unittest.main()