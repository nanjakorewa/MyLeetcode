import unittest
from problem1342 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass

    def test_normal_00(self):
        self.assertEqual(1, self.sol.numberOfSteps(1))

    def test_normal_01(self):
        self.assertEqual(6, self.sol.numberOfSteps(14))

if __name__ == "__main__":
    unittest.main()