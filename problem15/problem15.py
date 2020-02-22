from typing import List

# ナイーブに解く、時間切れ
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums):
                if i==j:
                    continue
                for k , nk in enumerate(nums):
                    if k==i or k==j:
                        continue

                    ans = [ni, nj, nk]
                    if sum(ans)==0:
                        ans.sort()
                        if not ans in res:
                            res.append(ans)

        return res