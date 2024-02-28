class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def generate(arr,idx):
            if idx==len(nums):
                return
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                ans.append(arr[:])
                generate(arr,i+1)
                arr.pop()

        generate([],0)
        return ans
            
        



