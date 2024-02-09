class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        postfix=[nums[-1]]
        res=[]
        

        for i in range(1,len(nums)):
          
            prefix.append(prefix[i-1]*nums[i])
            postfix.append(postfix[i-1]*nums[len(nums)-1-i])

        postfix.reverse()

        for i in range(len(nums)):
            if i==0:
                res.append(postfix[i+1])
            elif i==len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
    
        return res


        