class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l=0
        res=0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            print(charset)
            res=max(res, r-l+1)
        return res

# # {'p'}
# # {'w', 'p'}
# # {'w', 'p'}
# # {'w', 'k', 'p'}
# # {'w', 'k', 'e', 'p'}
# # {'w', 'k', 'e', 'p'}
        
# # "pwwkew"


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         mp = {}
#         l = 0
#         res = 0
        
#         for r in range(len(s)):
#             if s[r] in mp:
#                 l = max(mp[s[r]] + 1, l)
#             print(mp)
#             mp[s[r]] = r
#             res = max(res, r - l + 1)
#         return res


