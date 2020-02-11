class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        
        for (int i = 0; i < s.length(); i++) {
            if ((s[i] == '(') || (s[i] == '[') || (s[i] == '{')) {
                // 括弧の前半を見つけたらスタックに
                stk.push(s[i]);
            } else if (stk.size() == 0) {
                // スタックが空になるのは文字列の最後に到達した時のみ
                return false;
            } else {
                // 一番最後に見た括弧との対応を取る
                char top = stk.top();
                if (((s[i] == ')')&&(top != '(')) ||
                    ((s[i] == ']')&&(top != '[')) ||
                    ((s[i] == '}')&&(top != '{'))){
                    return false;
                }
                stk.pop();
            }
        }
        
        // スタックに括弧の残りが無ければValid
        return stk.size() == 0;
    }
};