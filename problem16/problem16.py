from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # resは絶対誤差：総和の辞書
        res = {}
        N = len(nums)

        nums.sort()
        tried_num = nums[0] - 1

        for l in range(N-2):
            # 一度調べた数字は結果が同じはずなのでスキップする
            if nums[l]==tried_num:
                continue
            else:
                tried_num = nums[l]

            # 探索対象の左・右端のインデックスを決める. i=左端のインデックス
            l = l + 1
            r = N - 1

            while l<r:
                # 和を求めて結果を保存
                total = tried_num+nums[l]+nums[r]
                #res.append(total)
                res[abs(target-total)] = total

                if total<target:
                    # 左を減らす
                    l += 1
                elif total>target:
                    # 右を減らす
                    r -= 1
                else:
                    # ターゲットと一致する
                    return target

        return res[min(res)]