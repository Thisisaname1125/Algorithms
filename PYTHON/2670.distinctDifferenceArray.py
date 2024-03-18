""" O(N^2)的实现稍微丑陋一点、 """
class Solution:
    def distinctDifferenceArray(self, nums):
        bagp = set()
        baga = set()
        ls = []
        for i in range(len(nums)):
            for j in nums[0: i+1]:
                bagp.add(j)
            for k in nums[i + 1:]:
                baga.add(k)
            ls.append(len(bagp) - len(baga))
            bagp.clear()
            baga.clear()
        return ls
    
if __name__ == "__main__":
    st = Solution()
    max = st.distinctDifferenceArray([1,2,3,4,5])
    print(max)