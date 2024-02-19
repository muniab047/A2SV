class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        counter=0
        for i in range(len(nums)-1,1,-1):
            right=i-1
            left=0
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    counter+=right-left
                    right-=1
                else:
                    left+=1
        return counter

            
           
            
        return counter

        