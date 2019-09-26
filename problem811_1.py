class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}

        # website domainごとに
        for cpdomain in cpdomains:
            countStr, domainsStr = cpdomain.split(" ")
            count = int(countStr)

            # 「.」で区切ったドメインのリスト
            domainsDotSplitted = [domainsStr]
            for i, si in enumerate(domainsStr):
                if si is ".":
                    # 「.」以降には必ず文字が存在する想定でいる
                    domainsDotSplitted.append(domainsStr[i+1:])

            # 集計
            for domain in domainsDotSplitted:
                if not domain in res:
                    res.update({domain:count})
                else:
                    res[domain] += count

        # 集計結果を出力のフォーマットに合わせる
        return [ "%s %s"%(v, k) for k, v in res.items()]
