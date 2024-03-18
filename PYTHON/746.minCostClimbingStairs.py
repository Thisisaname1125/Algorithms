""" 使用最小花费爬楼梯 """
""" 很简单，也没啥说的。 """
class Solution:
    # def recur(self, n, cost):
    #     if n == 0:
    #         return cost[0]
    #     if n == 1:
    #         return cost[1]
    #     return min(cost[n - 1], cost[n-2]) + cost[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = []
        minCost.append(cost[0])
        minCost.append(cost[1])
        for i in range(2, len(cost)):
            minCost.append(min(minCost[i-1],minCost[i-2]) + cost[i])
        return min(minCost[len(cost) - 1], minCost[len(cost) - 2])