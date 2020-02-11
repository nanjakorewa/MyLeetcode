class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: abs(x))
        return [x**2 for x in A]