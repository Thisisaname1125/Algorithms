# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240113 23:24
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 斐波那契数列 """
class Solution:
    def fib(self, n: int) -> int:
        f = []
        f.append(0)
        f.append(1)
        for i in range(2, n + 1):
            f.append(f[i-1]  + f[i-2])
        return f[n]