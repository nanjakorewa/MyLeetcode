import unittest
from problem1281_2 import Solution

class CheckSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        pass

    def tearDown(self):
        pass


    def test_normal_01(self):
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.assertEqual(0, self.sol.subtractProductAndSum(i))

    def test_normal_02(self):
        self.assertEqual(-1, self.sol.subtractProductAndSum(11))

    def test_normal_03(self):
        self.assertEqual(-1, self.sol.subtractProductAndSum(10**5))

if __name__ == "__main__":
    unittest.main()