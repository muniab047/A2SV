class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]

        for i in range(len(nums)):
            if(nums[i]>0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for j in range(len(pos)):
            ans.append(pos[j])
            ans.append(neg[j])

        return ans

        