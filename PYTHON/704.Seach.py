""" 二分法 """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        flag = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                flag = mid
                break
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return flag