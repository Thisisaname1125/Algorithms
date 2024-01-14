# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 22:47
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode

""" 83. 删去链表中重复的元素 """
# NOTE(Kun, 20240114):是20240113看了双指针操作后，20240114自己做出来的.

""" 双指针可解. """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        cur, exp = head, head.next
        while exp:
            if cur.val == exp.val:
                exp = exp.next
                cur.next = exp
            else:
                cur = exp
                exp = exp.next
        return head