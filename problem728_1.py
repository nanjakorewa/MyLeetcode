class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(right-left+1):
            # left~rightの範囲をチェック
            i += left
            flag = True
            stri = str(i)

            # 0が含まれていたらスキップ
            if "0" in stri:
                continue

            # 割り切れない場合は答えに含めない
            for i_n in str(i):
                if not i%int(i_n)==0:
                    flag = False
                    break

            # 全て割れた場合は追加
            if flag:
                res.append(int(i))

        return res