""" 不同路径 """
""" 也没啥说的, 挺简单的, 可能运行时间和运行内存待优化吧, 但是目前完全是自己写出来的 """
import numpy as np
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         """ np.intc是c中的int, np.uint是c中的无符号长整数."""
#         soltion = np.zeros((m, n), dtype=np.uint)
#         soltion[:, 0] = 1
#         soltion[0, :] = 1
#         for i in range(1, m):
#             for j in range(1, n):
#                 soltion[i, j] = soltion[i-1, j] + soltion[i, j-1]
#         return int(soltion[m - 1, n - 1])

# ==============================================================================================#
#       进阶版, 空间复杂度优化O(2n)
# ==============================================================================================#
""" 意识到了[1] * n是很有效的初始化方式.  """
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            """ note:(Kun, 20240116): 请关注如下两行代码 """
            # ==============================================================================================#
            #       pre = cur, 如果改变cur, pre也会变, 这个在一般的代码中是有些可怕的(但不排除有些代码可能恰恰需要
            #           这个功能, 但是极少吧可能/.)
            #       pre = cur[:], 相当于创建cur的副本给pre, cur变, pre不变.
            # ==============================================================================================#
            pre = cur[:]
            # pre = cur
        return cur[-1]
    
if __name__ == "__main__":
    s = Solution()
    s.uniquePaths(m = 3, n= 7)