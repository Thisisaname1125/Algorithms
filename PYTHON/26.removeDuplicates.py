class Solution:
    def removeDuplicates(self, nums) -> int:
        fast = 0
        C = 0
        count = 0
        numsSize = len(nums)
        for slow in range(0, numsSize - 1):
            fast = slow + 1
            import pdb
            pdb.set_trace()
            while(nums[fast] == nums[slow]):
                import pdb
                pdb.set_trace()
                count+=1
                fast+=1
            
            if(count > 0):
                while(fast < numsSize):
                    nums[fast-count] = nums[fast]
                    fast+=1
            C += count
            count = 0
        return C
if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))