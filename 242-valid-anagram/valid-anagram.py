# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False

## this has the time complexity of O(nlogn) --> for sorted array
## and space is O(n)

##Method 2: use counter ..this has time complexity of O(n) 
## and space complexity is O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)