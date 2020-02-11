class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        // ユニーク数だけ知りたいので集合に追加していく
        set<string> res;
        string mc[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        // wordsに含まれる単語それぞれをモールス信号に変換
        for (const auto& word : words) {
            string mc_word = "";
            for(int j = 0; j<word.length(); j++) mc_word += mc[word[j] - 'a'];
            res.insert(mc_word);
        }
        return res.size();
    }
};