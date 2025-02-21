class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l_p=0
        for i in range(len(nums)):
            #check y this code is not workimg
            # if nums[i]==val:
            #     nums[i]=nums[i+1]
            # nums[l_p]=nums[i]
            # l_p+=1
            if nums[i]!=val:
                nums[l_p]=nums[i]
                l_p+=1

        return l_p

               
    
        