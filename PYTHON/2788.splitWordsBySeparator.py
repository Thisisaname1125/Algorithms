""" 按分隔符拆分字符串、 """
""" 学习一下这里的写法、 """
class Solution:
    def splitWordsBySeparator(self, words, separator: str):
        return [s for w in words for s in w.split(separator) if s]
