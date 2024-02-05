class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=0

       
        while right<len(nums):
            if nums[right]!=val:
                nums[left], nums[right]=nums[right], nums[left]
                
                right+=1
                left+=1
            else:
                
                right+=1
        print(nums)
        

        if val in nums:
            return nums.index(val)
        else:
            return len(nums)