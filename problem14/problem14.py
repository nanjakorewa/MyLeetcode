class Solution:
    def longestCommonPrefix(self, strlist: List[str]) -> str:
        prefix = ""
            
        if len(strlist)==0:
            return ""
        elif len(strlist)==1:
            return strlist[0]
        else:
            # 文字列リストの先頭文字列と1文字ずつ調べる
            strlist.sort()
            for i, ci in enumerate(strlist[0]):
                flag = True
                for s in strlist[1:]:
                    if len(s)<=i:
                        # iよりも短い文字列なら終了
                        flag = False
                        break
                    elif s[i]==ci:
                        # 文字が一致した場合は次の文字列をチェック
                        continue
                    else:
                        # 一致しない場合は終了
                        flag = False
                        break

                if flag==False:
                    break
                else:
                    prefix += ci

            return prefix