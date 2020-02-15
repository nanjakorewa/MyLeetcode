import unittest
from problem1281 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass

    def test_normal_00(self):
        self.assertEqual(0, self.sol.subtractProductAndSum(0))

    def test_normal_01(self):
        self.assertEqual(0, self.sol.subtractProductAndSum(1))

    def test_normal_02(self):
        self.assertEqual(-1, self.sol.subtractProductAndSum(11))

    def test_normal_03(self):
        self.assertEqual(-1, self.sol.subtractProductAndSum(10**5))

if __name__ == "__main__":
    unittest.main()