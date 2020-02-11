class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        words = text.split(" ")
        if len(words)<2:
            return res
        else:
            for i, wordi in enumerate(words[:-2]):
                if wordi==first and words[i+1]==second:
                    res.append(words[i+2])
                else:
                    continue
        return res