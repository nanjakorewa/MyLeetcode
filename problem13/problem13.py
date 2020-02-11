class Solution:
    def romanToInt(self, s: str) -> int:
        ss = [   "M", "CM",   "D",  "CD",  "C", "XC",  "L", "XL",  "X", "IX", "V", "IV", "I"]
        vs = [1000,  900,  500,   400, 100,    90,   50,    40,   10,     9,     5,      4,   1]
        ind = 0
        res = 0
        slen = len(s)
        
        for sbl, val in zip( ss, vs ):
            # 末尾に到達したなら終了
            if ind==slen:
                break
            else:
                clen = len(sbl)
                while (s[ind:ind+clen]==sbl):
                    if s[ind:ind+clen]==sbl:
                        ind += clen
                        res += val
        return res