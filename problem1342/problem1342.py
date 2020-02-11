class Solution:
    def numberOfSteps (self, num: int) -> int:
        """/2と-1を何回行えば０になるかを求める

        Arguments:
            num {int} -- 数

        Returns:
            int -- /2, -1の適用回数
        """
        res = 0

        # /2 -1 を値が1になるまで繰り返す
        while(num>1):
            if num%2:
                num = num // 2
                res = res + 2
            else:
                num = num / 2
                res = res + 1

        # 1が余っている場合は+1して返す
        return int(res + num)
