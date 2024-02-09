class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=list(accumulate(nums))
        counter=0

        tracker=defaultdict(int)

        for num in prefix:
            if num-k==0:
                counter+=1
            if num-k in tracker:
                counter+=tracker[num-k]

            tracker[num]+=1

        return counter

        


        