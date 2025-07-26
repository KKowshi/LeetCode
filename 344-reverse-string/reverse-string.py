class Solution:
    def reverseString(self, s: List[str]) -> None:

        l, r= 0, len(s) -1  #0, 5

        while l<r:
            s[l],s[r] = s[r], s[l]
            #s[0], s[4] = s[4], s[0]
            l+=1 
            r-=1



        """
        Do not return anything, modify s in-place instead.
        """
        