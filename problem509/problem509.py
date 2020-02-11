class Solution:
    def fib(self, N: int) -> int:
        fibs = [0, 1]

        if N==0:
            return 0
        elif N<=2:
            return 1
        else:
            for i in range(N-2):
                fibs.append(sum(fibs[-2:]))
                fibs.pop(0)
            return sum(fibs[-2:])