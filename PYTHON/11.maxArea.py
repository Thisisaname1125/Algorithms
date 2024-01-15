# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240114 
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode

""" 盛最多水的容器 """
# ====================================================================================================================================#
#   经典题解：
#   https://leetcode.cn/problems/container-with-most-water/solutions/11491/container-with-most-water-shuang-zhi-zhen-fa-yi-do
#   内附算法正确性证明
#   NOTE(Kun, 20240114): 感觉很有意思, 算法力求直接找到最大值，证明证的是操作过程中不会略过最大值
#       感觉，算法和证明是两个思路逆着来的碰撞。精彩。
# ====================================================================================================================================#
""" 双指针可解. """

class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        maxarea = -1
        while left != right:
            
            area = min(height[left], height[right]) * (right - left)
            if area > maxarea:
                maxarea = area
            if height[left] <= height[right]:
                
                left += 1
            else:
                
                right -= 1
        return maxarea

if __name__ == "__main__":
    solution = Solution()
    height = [10,14,10,4,10,2,6,1,6,12]
    max = solution.maxArea(height=height)
    print(max)