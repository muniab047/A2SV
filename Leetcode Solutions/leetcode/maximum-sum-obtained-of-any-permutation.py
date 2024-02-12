class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mul=defaultdict(int)
        maximum=float('-inf')
        nums.sort(reverse=True)
        minimum=float('inf')
        ans=0

        for start,end in requests:
            mul[start]+=1
            mul[end+1]-=1
            maximum=max(maximum,end+1)
            minimum=min(minimum,start)
        cur=0
        for i in range(minimum,maximum+1):
            cur+=mul[i]
            mul[i]=cur
        a=list(mul.values())
        
        a.sort(reverse=True)
        print(a)
        print(nums)
        for i in range(min(len(a),len(nums))):
            ans+=a[i]*nums[i]
        return ans%(pow(10,9)+7)

        


