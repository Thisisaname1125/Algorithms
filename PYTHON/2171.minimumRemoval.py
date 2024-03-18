import sys
import numpy as np
# ===================================================================================#
#       NOTE(Kun, 20240119): 超时、
# ===================================================================================#
class Solution:
    """ 自研思路: 从0到length、到第i个的时候，前i-1个清零，i+1到length都和第i个对齐、 """
    def minimumRemoval(self, beans: List[int]) -> int:
        """  """
        minCount = sys.maxsize
        curCount = -1
        beansNumpy = np.array(beans)
        """  """
        beansNumpy.sort()
        """ 锚点、 """
        for i in range(len(beansNumpy)):
            """ np.sum """
            curCount = np.sum(beansNumpy[:i])
            delta = np.sum(beansNumpy[i + 1:] - beansNumpy[i])
            curCount = curCount + delta
            if curCount < minCount:
                minCount = curCount
        return int(minCount)

# =======================================================================#
#       通过、
# =======================================================================#   
import numpy as np
class Solution:
    """ 思路升级: 拿出去多少豆子 == (总数 - 剩余豆子数) """
    def minimumRemoval(self, beans: List[int]) -> int:
        """ sum、sort """
        beans.sort()
        total = sum(beans)
        mins = sum(beans)
        length = len(beans)
        for index in range(length):
            temp = total - (length - index) * beans[index]
            if temp <= mins:
                mins = temp
        return mins

