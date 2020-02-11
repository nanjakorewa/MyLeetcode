from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        itrs = [ii for i, ii in enumerate(nums) if i%2==0]
        vals = [vi for i, vi in enumerate(nums) if i%2==1]

        for itr, v in zip(itrs, vals):
            res += [v for _ in range(itr)]

        return res
