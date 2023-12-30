class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(1,len(nums)-1):
            if nums[i]+nums[i+1]>nums[i-1]:
                ans=nums[i-1]+nums[i]+nums[i+1]
                return ans

        return 0
      

  
        


