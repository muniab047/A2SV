class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums=defaultdict(int)
        maximum=float('-inf')
        for num,start,end in trips:
            nums[start]+=num
            nums[end]-=num
            maximum=max(maximum,end)
        for i in range(maximum+1):
            nums[i]=nums[i]+nums[i-1]
            if nums[i]>capacity:
                return False
        return True
            
        