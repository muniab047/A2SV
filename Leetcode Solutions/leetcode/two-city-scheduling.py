class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        adiff=[]
        bdiff=[]
        
        summ=0
        acounter=0
        bcounter=0
        for cost in costs:
            a,b=cost
            
            minimum=min(a,b)
            if minimum==a:
                acounter+=1
                bdiff.append(b-a)
            else:
                bcounter+=1
                adiff.append(a-b)
            summ+=minimum

        adiff.sort()
        bdiff.sort()
        n=abs(acounter-((acounter+bcounter)//2))

        print(acounter,bcounter,n)
        \
        print(summ)
        
        for i in range(n):
            if acounter>bcounter:
            
                summ+=bdiff[i]
                
            else:
                summ+=adiff[i]

        return summ

        






        
        return summ

        