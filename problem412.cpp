class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res(n);
        
        for(int i=0;i<n;i++){
            int ip1 = i+1;
            if(ip1%3==0 || ip1%5==0){
                if(ip1%3==0)res[i]+="Fizz";
                if(ip1%5==0)res[i]+="Buzz";   
            } else {
                res[i]+=to_string(ip1);
            }
        }
        return res;
    }
};