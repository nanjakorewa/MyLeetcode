class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        textlen = len(text)
        res = []

        if textlen>1:
            for i in range(textlen-2):
                if text[i]==first and text[i+1]==second:
                    res.append(text[i+2])
        return res