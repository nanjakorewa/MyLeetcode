class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;
        for(const int n : nums)
            if (int(std::log10(n)+1)%2 == 0)
                res += 1;
        return res;
    }
};