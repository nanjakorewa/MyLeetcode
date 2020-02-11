class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        cnt = 0

        for s in S:
            if s=="(":
                cnt+=1
                if cnt>1:res+=s
            else:
                if cnt>1:res+=s
                cnt-=1
        return res