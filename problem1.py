from typing import Callable
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        srt = nums.copy()
        n = len(srt)
        srt.sort()

        for i, si in enumerate(srt):
            for j in range(n-1-i):
                if si+srt[n-1-j]>target:
                    continue
                else:
                    break
            if si+srt[n-1-j]==target:
                break
            else:
                continue

        if si==srt[n-1-j]:
            return
        ans1 = nums.index(si)
        nums[ans1] = -0.1
        ans2 = nums.index(srt[n-1-j])

        return [ans1, ans2]
