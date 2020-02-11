class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int res = 0;
        auto sortedh {std::vector<int>(heights)};
        std::sort(sortedh.begin(), sortedh.end());

        for(size_t i=0; i<sortedh.size(); i++)
            if(sortedh[i]!=heights[i]) res++;

        return res;
    }
};