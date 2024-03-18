""" 有效的括号、 """
""" dict可以直接用[]索引, 但索引key不存在会报错。如果用.get()索引就会返回none """
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = dict({"(":")", "[":"]", "{":"}"})
        for char in s:
            if len(l) != 0:
                p = l.pop()
                if d.get(p) == char:
                    continue
                else:
                    l.append(p)
                    l.append(char)
            else:
                l.append(char)
        return not len(l)