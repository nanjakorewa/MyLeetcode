class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(right-left+1):
            stri = str(i+left)
            if not "0" in stri and all(((i+left)%int(i_n)==0 for i_n in stri)):
                res.append(i+left)

        return res