# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 23:17
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 爬楼梯 """

class Solution:
    def climbStairs(self, n: int) -> int:
        solution = []
        solution.append(0)
        solution.append(1)
        solution.append(2)
        for i in range(3, n + 1):
            """ 关键. """
            solutionNum = solution[i-1] + solution[i-2]
            solution.append(solutionNum)
        return solution[n]