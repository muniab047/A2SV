class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ls=[]
        l = 0
        r = 2
        while r < len(num):
            s = num[l:r+1]
            t = set(s)
            if len(t) == 1:
                ls.append(s)
            l+=1
            r+=1

        return max(ls, default="")


       
               

            

       

            

       
        


        