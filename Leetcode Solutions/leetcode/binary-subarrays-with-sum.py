class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur=0
        prefix=[]
        subarr=0
        for num in nums:
            cur+=num
            prefix.append(cur)
        tracker=defaultdict(int)
        for i in range(len(prefix)):
            if prefix[i]==goal:
                subarr+=1
            if tracker[prefix[i]-goal]>0:
                subarr+=tracker[prefix[i]-goal]
            tracker[prefix[i]]+=1
        return subarr

