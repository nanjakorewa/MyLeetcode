class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx, by = bin(x)[2:], bin(y)[2:]
        ndigit = len(bx) if x>=y else len(by)
        bx, by = bx.zfill(ndigit), by.zfill(ndigit)
        return sum([xi!=yi for xi, yi in zip(bx, by)])