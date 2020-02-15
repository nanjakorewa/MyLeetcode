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

        while(n>0):
            i = n%10
            num_sum += i
            num_prd *= i
            n = int(n/10)

        return num_prd-num_sum