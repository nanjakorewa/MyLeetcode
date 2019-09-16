class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        head, tail = A[0], A[-1]
        A = [x**2 for x in A]

        if head>=0:
            return A
        elif tail<=0:
            return reversed(A)
        else:
            A.sort()
            return A