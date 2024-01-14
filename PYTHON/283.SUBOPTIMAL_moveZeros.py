# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 23:24
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
# =====================================================================#
# @RevisedTime: 

""" NOTE(Kun,20240113): 既然使用双指针解法, 就一定要保证后指针不能在前指针的前面. """
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Index1 = 0 # 待填补的第一个
        Index2 = 0 # 
        while Index2 < len(nums) and Index1 < len(nums):
            if nums[Index1] == 0:
                if nums[Index2]:
                    nums[Index1] = nums[Index2]
                    nums[Index2] = 0
                    Index2 += 1
                elif nums[Index2] == 0:
                    Index2 += 1
            else:
                Index1 += 1
                """ note:粗糙的保证法、 """
                Index2 = Index1