class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def bisectleft(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2

                if nums[mid] < target:
                    left=mid+1
                else:
                    right=mid-1
            return left
            

        def bisectright(nums, target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid] <= target:
                    left=mid+1
                else:
                    right=mid-1
            return right
        left=bisectleft(nums,target)
        right=bisectright(nums, target)

        if left>right:
            return [-1,-1]

        return [left,right]


        
        


        