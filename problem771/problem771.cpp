class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        set<char> cJ(J.begin(), J.end());
        for (char s : S) {
            if (cJ.count(s)) res++;
        }
        return res;
    }
};