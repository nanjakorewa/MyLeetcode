class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -1*int(str(x)[::-1][:-1])
            
        return (-2147483649<x<2147483649)*x