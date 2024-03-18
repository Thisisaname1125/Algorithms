class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        results=[]

        for i in range(0, N-2):
            if nums[i] > 0:
                break
            if(i > 0 and nums[i]==nums[i-1]):
                continue
            target = -nums[i]
            slowp, fastp = i+1, N-1
            while slowp < fastp:
                if nums[slowp] + nums[fastp] > target:
                    fastp -= 1
                elif nums[slowp] + nums[fastp] < target:
                    slowp += 1
                else:
                    results.append((nums[i], nums[slowp], nums[fastp]))
                    while slowp < fastp and nums[slowp] == nums[slowp+1]:
                        slowp = slowp + 1
                    while slowp < fastp and nums[fastp] == nums[fastp-1]:
                        fastp = fastp - 1
                    slowp += 1
                    fastp -= 1



        # slow, quick = 0, 1
        # while slow < len(results):
        #     if quick == len(results):
        #         slow += 1
        #         quick = slow + 1
        #         continue
        #     if results[slow] == results[quick]:
        #         results.pop(quick)
        #     else:
        #         quick += 1
        return results

