class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        index=sorted(list(set(nums)))
        dic=defaultdict()
        counter=0
        for i in range(len(index)):
            dic[index[i]]=i

        for num in nums:
            counter+=dic[num]
        return counter

        