class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        res= -1 

        for n in arr:
            freq[n] = 1+ freq.get(n,0)

        for k,v in freq.items():
            if k==v:
                res = max(res, k)

        return res 
        