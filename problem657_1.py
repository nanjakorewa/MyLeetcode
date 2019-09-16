class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 各動作の動きの定義
        ms = {"R":[1,0], "L":[-1,0], "U":[0,1], "D":[0,-1]}
        x, y = 0, 0

        # x/yを移動させる
        for mv in moves:
            m = ms[mv]
            x += m[0]
            y += m[1]

        return x==y==0