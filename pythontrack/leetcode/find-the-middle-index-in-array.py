class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum=nums
        leftsum=0

        for i in range(1,len(nums)):
            prefixSum[i]=prefixSum[i]+prefixSum[i-1]
        for i in range(len(nums)):
            if leftsum==prefixSum[len(nums)-1]-prefixSum[i]:
                return i
            else:
                leftsum=prefixSum[i]
            
        return -1

        


        