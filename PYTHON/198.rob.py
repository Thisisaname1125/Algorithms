""" 打家劫舍, 很简单，也没啥说的 """
""" 简单说说, 如果确定第k家要抢, 那抢完第k家带来的总利润一定是
 (从第0家到第k-2家最大的总利润+ 当前这家的利润)
最后返回是从总利润列表的倒数两个里面选一个."""
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        money = []
        money.append(nums[0])
        money.append(nums[1])
        
        for i in range(2, length):
            money.append(max(money[:i-1]) + nums[i])

        return max(money[length-1], money[length-2])
