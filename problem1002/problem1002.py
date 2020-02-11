class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        wordLengthList = [len(a) for a in A]
        mostShortWord = A[wordLengthList.index(min(wordLengthList))]

        for ci in mostShortWord:
            for i, ai in enumerate(A):
                if ci in ai:
                    A[i] = ai.replace(ci, '', 1)
                    continue
                else:
                    ci = ''
                    break

            if not ci=='':
                res.append(ci)

        return res