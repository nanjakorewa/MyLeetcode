# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 28 ms, faster than 72.25% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.9 MB, less than 98.48% of Python3 online submissions for Swap Nodes in Pairs.

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        p = head
        while(p is not None):
            if p.next is None:
                break  # 入力が奇数長だった場合

            temp = p.next.val
            p.next.val = p.val
            p.val = temp

            p = p.next.next

        return head
