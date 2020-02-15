class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """入力の各桁の掛け算と足し算の差分を返す

        Arguments:
            n {int} -- 自然数(1<=n<=10^5)

        Returns:
            int -- answer
        """

        num_sum = 0
        num_prd = 1

        # もしもn<0のケースがある場合
        # if n<0:
        #   num_sum = int(str([:2]))
        #   num_prd = -1

        for num in str(n):
            num = int(num)
            num_sum+=num
            num_prd*=num

        return num_prd-num_sum