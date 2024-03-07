class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix=list(accumulate(nums))

        min_=0
        ans=[]

        for num in prefix:
            ans.append(num-min_)
            min_=min(min_, num)
        return max(ans)


        