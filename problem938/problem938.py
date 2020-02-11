# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        self.res = 0

        def search(node):
            if node is not None:
                nv = node.val
                if L <= nv <= R:self.res += node.val
                if L < nv:search(node.left)
                if nv < R:search(node.right)

        search(root)
        return self.res