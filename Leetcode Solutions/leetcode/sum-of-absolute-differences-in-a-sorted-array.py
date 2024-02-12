class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        curpre=0
        curpos=0
        prefix=[]
        postfix=[]
        res=[]

        for i in range(len(nums)):
            curpre+=nums[i]
            curpos+=nums[len(nums)-i-1]
            prefix.append(curpre)
            postfix.append(curpos)
        postfix.reverse()
        for i in range(len(nums)):
            
            if i<len(nums)-1:
                ans=abs(prefix[i]-(nums[i]*(i+1)))+postfix[i+1]-(nums[i]*(len(nums)-i-1)) 
            else:
                ans=abs(prefix[i]-(nums[i]*(i+1)))       
            res.append(ans)
        return res

    