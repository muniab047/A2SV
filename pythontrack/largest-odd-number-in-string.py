class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=''

        for i in range(len(num)):
            j=len(num)-i
            if(int(num[j-1])%2!=0):
                ans+=num[0:j]
                break
        
            
        return ans
        