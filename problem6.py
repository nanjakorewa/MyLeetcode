class Solution(object):
    def convert(self, s, numRows):
        # ジグザグにならないのでそのまま返す
        if numRows <= 1:
            return s
        
        n = len(s)
        if n <= 1:
            return s
        
        # 各行の文字列を連結する
        index = 2*numRows - 2
        res = ''
        for i in range(numRows):
            for j in range(i, n, index):
                res += s[j]
                if i==0:
                    continue
                elif i!=numRows-1 and j+index-i*2<n:
                    res += s[j+index-i*2]
        return res