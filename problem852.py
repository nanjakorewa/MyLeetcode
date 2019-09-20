class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i, ai in enumerate(A):
            if A[0]<=ai:A[0]=ai
            else:return i-1