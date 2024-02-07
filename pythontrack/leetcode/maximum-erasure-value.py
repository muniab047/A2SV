class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        maxSum=float('-inf')
        counter=defaultdict(int)
        summ=0

        while left<len(nums) and right<=len(nums):
        
            if right<len(nums) and counter[nums[right]]<1:
                counter[nums[right]]+=1
                summ+=nums[right]
                maxSum=max(maxSum,summ)
                right+=1
            else:
                summ-=nums[left]
                counter[nums[left]]-=1
                left+=1

        return maxSum

        