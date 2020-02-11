class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([ni for i, ni in enumerate(nums) if i%2==0])