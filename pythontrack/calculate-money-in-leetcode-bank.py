class Solution:
    def totalMoney(self, n: int) -> int:
        start=0
        counter=1
        summ=0
        for i in range(1,n+1):
            if(i%7==1):
                start+=1
                counter=start
            summ+=counter
            counter+=1

        return summ


            





        