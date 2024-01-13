# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 22:47
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode

""" pass """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)
                    return solution


# =========================================================================#
#        1. python中的dict()是基于哈希表实现的
#        2. enumerate从0开始
#        3. if x in 某个字典，查的是x是不是该字典的key.      
# =========================================================================#       

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 1. python中的dict()是基于哈希表实现的 """
        hashT = dict()
        """ 2. enumerate从0开始 """
        for i, num in enumerate(nums):
            """ 3. if x in 某个字典, 查的是x是不是该字典的key. """
            if target-num in hashT:
                return [hashT[target-num], i]
            hashT[num] = i
