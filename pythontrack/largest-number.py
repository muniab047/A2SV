class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums=[str(num) for num in nums]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(nums[i]+nums[j],nums[j]+nums[i])
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i],nums[j]= nums[j],nums[i]

        st=''.join(nums)
        if int(st)==0:
            return '0'
        return st
        

        
      
        