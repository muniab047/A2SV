class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)

        def findPartition(mid):
            counter=1
            sum_=0
            for i in range(len(nums)):
                if sum_+nums[i]>mid:
                    sum_=0
                    counter+=1
                    sum_+=nums[i]
                else:
                    sum_+=nums[i]
            return counter

        while left<=right:
            mid=(left+right)//2

            partition=findPartition(mid)

            if partition<=k:
                right=mid-1
            else:
                left=mid+1
        return left
        