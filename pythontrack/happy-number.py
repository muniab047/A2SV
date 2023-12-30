class Solution:
    def isHappy(self, n: int) -> bool:
        n=abs(n)
        s=str(n)
        res=''
        x=n
        start=0
        for i in range(len(s)):
            start+= int(s[i])**2

        

        s=str(start)
        end=0
        seen = set()


        while(start!= end):
            # print(start,end,start==end)
        # for j in range(100):
            end=0
            for i in range(len(s)):
                end += int(s[i])**2

            if(end==1):
                return True
            elif end in seen:
                return False
            seen.add(end)

           # print(s)

            s= str(end)
            

        return False
       




            

        


        


        

        

        




        