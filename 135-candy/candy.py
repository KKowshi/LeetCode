class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        #checking forthe empty array
        if n==0:
            return 0

        #increasingpass
        left= [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1

        #non-decreasingpass
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                left[i] = max(left[i], left[i+1]+1)

        return sum(left)


        



        