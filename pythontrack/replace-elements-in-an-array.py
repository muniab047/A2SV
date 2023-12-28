class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={}

        for i in range (len(nums)):
            d[nums[i]]=i

        for op in operations:
            x,y=op
            index = d[x]
            d.pop(x)
            d[y]=index
            nums[index] = y

        return nums

       

        


        
        