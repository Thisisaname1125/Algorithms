# -*- coding: utf-8 -*- 
# @Author: Kun
# @Time: 20240114 
# @Email: zhaozk_bjtu@163.com
# @Software: Vscode
""" 回文数 """
""" 字符串版本，双指针可解. """
class SolutionStr:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        left, right = 0, len(strx) - 1
        Flag = True
        while left <= right:
            if strx[left] == strx[right]:
                left += 1
                right -= 1
            else:
                Flag = False
                return Flag
        return Flag
    
""" 字符串版本的骚操作 """
class SolutionStrS:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
# =============================================================#
#       进阶版. 不转字符串.
# =============================================================#
""" 核心思想：逆转一半数字 """
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ 负数肯定不行 """
        if x < 0:
            return False
        """ 最后一位是0的, 除了0以外肯定不行. """
        if x % 10 == 0 and x // 10 != 0:
            return False
        reverse = x % 10
        x = x // 10

        """ 思考过: 判断位数处理到一半, 到位数之前, x > reverse依据如下 """
        """ 若奇数位, 只要左边的位数大于右边, 肯定满足x > reverse. """
        """ 若偶数位, 分T与F. """
        # =====================================================================#
        #       一、T，则到位置之前肯定x > reverse, 到位置就等于，跳出
        #       二、F，则到位置之前肯定x > reverse, 毕竟位数大就是大，100也比99大
        #           到位置之后又分为两种情况：x < reverse, 满足假设
        #           到位置之后, x还是大于> reverse, 比如654321，=======这个确实是官方题解逻辑上的一个漏洞.
        #           但是，接下面是接的通的，再处理一位，跳出，还是满足False这个.
        # =====================================================================#
        """ 其实这个循环是为好数设计的, 因为坏数, 第一位肯定就不等了啊. 也就无所谓判断终点之类的了. """
        while x > reverse:
            reverse = reverse *10 + x % 10
            x = x // 10

        """ 最终判据. """
        if reverse == x or reverse // 10 == x:
            return True
        else:
            return False



if __name__ == "__main__":
    solution = SolutionStrS()
    max = solution.isPalindrome(12321)
    print(max)