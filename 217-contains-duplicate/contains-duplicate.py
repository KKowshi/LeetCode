class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num={}
        for i in nums:
            if i in num:
                return True

            num[i] = i 
        return False

        