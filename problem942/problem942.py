class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        nmin, nmax = -1, 1
        res = [0]

        for IorD in S:
            if IorD=="D":
                res.append(nmin)
                nmin -= 1
            else:
                res.append(nmax)
                nmax += 1

        return [n-nmin-1 for n in res]