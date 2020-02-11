/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        search(root, L, R);
        return res;
    }
    
    int res = 0;
    
    void search(TreeNode* root, int L, int R){
        if (root==nullptr){
            return;
        } else {
            if (L<=root->val && root->val<=R){
                res += root->val;
            }
            if (L<root->val) search(root->left, L, R);
            if (root->val<R) search(root->right, L, R);
        }
    }
};