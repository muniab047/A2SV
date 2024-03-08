class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        best=0

        while left<=right:
            mid=(left+right)//2

            if nums[mid]>=nums[best]:
                left=mid+1
            else:
                best=mid
                right=mid-1
                
        return nums[best]
            
        