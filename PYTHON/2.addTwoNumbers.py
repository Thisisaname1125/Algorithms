# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
""" 两数相加 """
""" 一定要搞什么递归吗? 看我粗暴时复O(N) + 空复O(N)解法、 """
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1p = l1
        l2p = l2

        dummy = ListNode()
        p = dummy
        redund = 0

        while l1p and l2p:
            nw = ListNode()
            if redund == 1:
                nw.val = l1p.val + l2p.val + 1
                redund = 0
            else:
                nw.val = l1p.val + l2p.val

            if nw.val >= 10:
                redund = 1
                nw.val = nw.val % 10
            p.next = nw
            p = p.next
            l1p = l1p.next
            l2p = l2p.next
        
        while l1p:
            nw = ListNode()
            if redund == 1:
                nw.val = l1p.val + 1
                redund = 0
            else:
                nw.val = l1p.val

            if nw.val >= 10:
                redund = 1
                nw.val = nw.val % 10
            p.next = nw
            p = p.next
            l1p = l1p.next

        while l2p:
            nw = ListNode()
            if redund == 1:
                nw.val = l2p.val + 1
                redund = 0
            else:
                nw.val = l2p.val

            if nw.val >= 10:
                redund = 1
                nw.val = nw.val % 10
            p.next = nw
            p = p.next
            l2p = l2p.next

        if redund == 1:
            nw = ListNode()
            nw.val = 1
            p.next = nw

        return dummy.next