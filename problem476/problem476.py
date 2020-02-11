class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        for b in bin(num)[2:]:
            if b=="0":res += "1"
            else:res += "0"
        return int(res, 2)