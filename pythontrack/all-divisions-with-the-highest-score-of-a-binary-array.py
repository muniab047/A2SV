class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        maxi=0
        nr=sum(nums)
        nl=0
        


        for i in range(len(nums)+1):
            if(i>0):
                if(nums[i-1]==1):
                    nr-=1
                if(nums[i-1]==0):
                    nl+=1

            na=nl+nr

            dic[na].append(i)
            
            if(na>maxi):
                maxi=na

        return dic[maxi]

        