class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for r in A:
            r.reverse()
            res.append([1-ri for ri in r])
        return res