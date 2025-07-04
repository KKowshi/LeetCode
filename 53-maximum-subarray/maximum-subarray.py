class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum =0

        #[-2,-1,]

        for n in nums: #-2, -1
            if curr_sum<0:
                curr_sum=0 #0
            curr_sum+=n # -1

            max_sum = max(max_sum, curr_sum) #-1

        return max_sum


        