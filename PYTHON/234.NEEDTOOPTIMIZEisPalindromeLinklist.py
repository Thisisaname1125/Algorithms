# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240114 
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 回文链表 """
""" 解法简单: 把链表中的值拼成字符串, 按照回文字符串的方式判断即可 """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        strz = ''
        while cur != None:
            strz+=str(cur.val)
            cur = cur.next
        return strz==strz[::-1]
    
# =============================================================#
#       进阶版. O(n)时间复杂度, O(1)空间复杂度.
# =============================================================#
""" 待写... """