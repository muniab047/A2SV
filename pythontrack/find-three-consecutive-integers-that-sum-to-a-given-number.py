class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]

        if(num%3==0):
            y=num//3
            ans.append(y-1)
            ans.append(y)
            ans.append(y+1)
        return ans
       

        