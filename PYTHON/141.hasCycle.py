# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" 环形链表、 """
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        bag = set()
        while head:
            if head in bag:
                return True
            else:
                bag.add(head)
                head = head.next
        return False