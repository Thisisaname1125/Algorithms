""" 第N个泰波那契数, 没啥难度，不多写了/. """
class Solution:
    def tribonacci(self, n: int) -> int:
        solution = []
        solution.append(0)
        solution.append(1)
        solution.append(1)
        for i in range(3, n + 1):
            solution.append(solution[i -1]+solution[i-2]+solution[i-3])
        return solution[n]