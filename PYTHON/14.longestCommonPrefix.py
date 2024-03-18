""" 最长公共前缀、 """
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            index = 0
            while index < len(prefix) and index < len(string) and prefix[index] == string[index]:
                index += 1
            prefix = prefix[:index]
        return prefix