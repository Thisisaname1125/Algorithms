class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count = count + 1 if num == candidate else count - 1
        return candidate

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,3,4]))