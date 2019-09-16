class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 奇数回では戻れないので返す
        if len(moves)%2==1:return False
        # 各動作の出現回数
        ms = {"R":0, "L":0, "U":0, "D":0}
        # 各動作の出現回数をカウント
        for mv in moves:ms[mv]+=1
        return ms["R"]==ms["L"] and ms["U"]==ms["D"]