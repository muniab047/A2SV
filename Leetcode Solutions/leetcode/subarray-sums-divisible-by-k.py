class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        pre = list(accumulate(nums))
        left=0
        counter=0
        tracker=defaultdict(int)

        for i in range(len(nums)):
            if pre[i]%k==0:
                counter+=1
            if pre[i]%k in tracker:
                counter+=tracker[pre[i]%k]
            tracker[pre[i]%k]+=1
        return counter
            
