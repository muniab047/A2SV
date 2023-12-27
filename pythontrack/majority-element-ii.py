class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=set()

        for i in range(len(nums)):
            if(nums.count(nums[i])>len(nums)/3 ):
                ans.add(nums[i])

        return ans

        