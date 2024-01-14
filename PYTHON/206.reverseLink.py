# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 23:42
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 反转链表 """

""" 双指针可解. """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre