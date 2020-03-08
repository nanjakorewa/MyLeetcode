class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        cnt = 0

        while(cnt<len(nums)):
            if nums[cnt]==val:
                del nums[cnt]
                continue
            else:
                cnt = cnt + 1

        return cnt