class Solution:
    def myAtoi(self, str: str) -> int:
        s = 1
        res, i = "", 0
        
        # Noneの場合0
        if str is None:
            return 0
        n = len(str)
        
        # 空白行を読み飛ばす
        while i < n and str[i] == ' ':
            i += 1
            
        # 初めの符号をチェックする
        if i < n and str[i] == '-':
            s = -1
            i += 1
        elif i < n and str[i] == '+':
            i += 1
            
        # 数値の読み取りをする
        while i < n and str[i].isdigit():
            res += str[i]
            i += 1
            
        # 数値がない場合は0
        if len(res)==0 or n==0:
            return 0
        
        # ３２ビット幅の確認
        res = s * int(res)
        if res < -2147483648:
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        else:
            return res