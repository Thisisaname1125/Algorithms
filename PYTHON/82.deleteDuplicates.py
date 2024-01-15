# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240115 21:18
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 删除排序链表中的重复数据. """

# ==================================================================================#
#       NOTE(Kun, 20240115): 学到了一招哑结点.dummy node
# ==================================================================================#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not cur:
            return cur
        dummy = ListNode(0, head)
        cur = dummy
        x = -5
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next