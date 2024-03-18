""" 最小路径和, 没啥难度 """
# ==========================================================================================#
#       \item. axis = 0是向下出发，即纵轴；axis = 1是向右出发，即横轴.
#       \item. np.cumsum是算累积和，第一个数即第一个数，第二个数即第二个数加第一个数，以此类推.
# ==========================================================================================#
import numpy as np
class Solution:
    def minPathSum(self, grid) -> int:
        gridNumpy = np.array(grid)
        m = len(grid)
        n = len(grid[0])
        count = np.zeros((m, n), dtype = np.uint)
        count[0, :] = np.cumsum(gridNumpy[0, :])
        count[: , 0] = np.cumsum(gridNumpy[:, 0])
        for i in range(1, m):
            for j in range(1, n):
                count[i, j] = min(count[i-1,j], count[i, j-1]) + gridNumpy[i,j]
        return int(count[m-1, n-1])
if __name__ == "__main__":
    s = Solution()
    s.minPathSum(grid = [[1,2,3],[4,5,6]])