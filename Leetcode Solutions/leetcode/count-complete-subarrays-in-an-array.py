class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter=Counter()
        s=set(nums)

        left=0
        right=0
        counter=0

        while right<=len(nums) and left<len(nums):
            if set(nums[left:right])!= s:
                right+=1
            else:
                counter+=(len(nums)-right+1)
                left+=1
        return counter
                



        