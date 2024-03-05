class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        prefix=list(accumulate(nums))

        tracker=defaultdict(int)
        counter=0

        for num in prefix:
            if num-k==0:
                counter+=1
            if num-k in tracker:
                counter+=tracker[num-k]

            tracker[num]+=1

        return counter
        




