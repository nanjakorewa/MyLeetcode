# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def mergetree(node1, node2):
            if node1 is None:
                return node2
            elif node2 is None:
                return node1
            else:
                node = node1
                node.val = node1.val + node2.val
                node.left = mergetree(node1.left, node2.left)
                node.right = mergetree(node1.right, node2.right)
                return node

        return mergetree(t1, t2)