class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mmap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        oda, odz = ord("a"), ord("z")

        for word in words:
            mc_word = ""
            for c in word:
                od = ord(c)
                mc_word += mmap[od-97]
            res.append(mc_word)

        return len(set(res))