class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;
        for(const int n : nums){
            size_t len = std::to_string(n).length();
            if (len%2==0) res += 1;
        }
        return res;
    }
};