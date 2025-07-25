class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r= len(needle)
        ans = 0
        for i in range(0,len(haystack)):
            if haystack[i:i+r] == needle:
                return i
        return -1 
        