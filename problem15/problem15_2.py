from typing import List

# ナイーブに解く、時間切れ
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N<2:return []

        # +/-で分ける
        positives = [n for n in nums if n>0]
        negatives = [n for n in nums if n<=0]

        # 0-0-0のケース
        zeros = [z for z in negatives if z ==0]
        if len(zeros)>2:
            result.append([0, 0, 0])

        # 先にソートして重複した解答が出ないようにする
        positives.sort()
        negatives.sort()

        # 足すとtargetになるペアをlから取得する
        def _get_pairs(l, target):
            res = []
            for i, li in enumerate(l[:N-1]):
               for j, lj in enumerate(l[i+1:]):
                   if (li+lj)==target:
                        res.append([li, lj])
            return res

        # 答えを集める
        result = []
        for p in positives:
            result += [ [p]+pair for pair in _get_pairs(negatives, -p)]
        for n in negatives:
            result += [ [n]+pair for pair in _get_pairs(positives, -n)]

        # 重複を取り除く
        res = []
        for r in result:
            r.sort()
            if not r in res:
                res.append(r)

        return res