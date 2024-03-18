class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        res = 0
        neg = 0
        if x < 0:
            neg = 1
            x = abs(x)
        while x != 0:
            res = x % 10
            x = x // 10
            num = num * 10 + res
        if neg == 1:
            num = -num
        if num < -2^31 or num > 2 ^ 31 -1:
            import pdb
            pdb.set_trace()
            return 0
        return num

if __name__ == "__main__":
    print(Solution().reverse(123))