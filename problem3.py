class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 最大の部分列長、現在保持してる部分列
        result, sub = 0, ""
        for char in s:
            if char not in sub:
                # 部分列に含まれないcharならば追加
                sub += char
                result = max(result, len(sub))
            else:
                # 部分列の中で最初に見つかるcharの箇所まで切り落とす
                sub = sub[sub.index(char)+1:] + char
        return result
