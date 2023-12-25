class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            nums2=nums[i+1:]
            if nums2.count(target-nums[i])==1:
                ans.append(i)
                ans.append(nums2.index((target-nums[i]))+i+1)
                return ans


        