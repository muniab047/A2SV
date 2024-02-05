class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        minValue=float('inf')
        summ=0

        while left<len(nums) and right<=len(nums):
            if summ<target:
                if right<len(nums):
                    summ+=nums[right]
                right+=1
            else:
                length=right-left
                minValue=min(minValue,length)
                summ-=nums[left]
                left+=1

        if minValue== float('inf'):
            return 0
        else:
            return minValue
        


        