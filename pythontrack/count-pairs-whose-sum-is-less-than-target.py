class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        counter=0
        nums.sort()

        while start<end:
            if nums[start]+nums[end]<target:
                counter+=end-start
                start+=1
            elif nums[start]+nums[end]>=target:
                end-=1

        return counter
            
        