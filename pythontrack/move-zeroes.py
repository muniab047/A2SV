class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place=0
        index=0
        while index<len(nums):
            
            if nums[index]!=0:
                nums[index],nums[place]= nums[place],nums[index]
                place+=1
            index+=1
            
            
            
        