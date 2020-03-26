# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 16 ms, faster than 99.78% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13 MB, less than 96.97% of Python3 online submissions for Swap Nodes in Pairs.
# Next challenges:

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        def swapNext(head):
            if head is None:
                return None
            elif head.next is None:
                return None
            else:
                temp = head.next.val
                head.next.val = head.val
                head.val = temp
                swapNext(head.next.next)

        swapNext(head)
        return head
