class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        if x<0:
            return False
        else:
            x = str(x)
            res = True
            # 左右対称かチェック、中央はチェック不要
            for i in range(len(x)//2):
                res = res and (x[i]==x[-1+-1*i])
                
            return res