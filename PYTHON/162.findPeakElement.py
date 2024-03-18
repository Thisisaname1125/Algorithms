""" 寻找峰值\ """
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get(index):
            if index == -1 or index == n:
                """ 负无穷的表示、 """
                return float('-inf')
            return nums[index]
        left, right, ans = 0, n-1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            elif get(mid) > get(mid + 1):
                """ 为什么是mid-1不是mid呢，因为第一个if已经排除了get(mid)在山峰上，
                因此get(mid-1)一定更大于get(mid) """
                right = mid -1
            elif get(mid) < get(mid + 1):
                left = mid + 1
        