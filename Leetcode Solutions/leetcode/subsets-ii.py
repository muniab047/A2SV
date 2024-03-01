class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans=set()
        ans.add(())
        arr=[]

        def generateSubset(idx):

            for i in range(idx,len(nums)):
                arr.append(nums[i])
                ans.add(tuple(arr[:]))
                generateSubset(i+1)
                arr.pop()

        generateSubset(0)
        return ans

        