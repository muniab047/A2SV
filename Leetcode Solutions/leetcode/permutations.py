class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        choosen=[False]*len(nums)

        def perm(arr):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return

            for i in range(len(nums)):
                if not choosen[i]:
                    arr.append(nums[i])
                    choosen[i]=True
                    perm(arr)
                    choosen[i]=False
                    arr.pop()
        perm([])
        return ans



        