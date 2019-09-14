class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = 0

        # calc l1 + l2
        counter = 0
        while True:
            ans += 10**counter*l1.val
            if not l1.next is None:
                counter += 1
                l1 = l1.next
            else:
                break

        counter = 0
        while True:
            ans += 10**counter*l2.val
            if not l2.next is None:
                counter += 1
                l2 = l2.next
            else:
                break

        # answer, 逆順に入れる
        l1 = l2 = ListNode(0)
        for ci in str(ans)[::-1]:
            l2.next = ListNode(int(ci))
            l2 = l2.next

        return l1.next
