class Solution:
    def bestClosingTime(self, customers: str) -> int:
        openpenality=[]
        closepenality=[]
        penality=[]

        sum_=0
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=='Y':
                sum_+=1
            closepenality.append(sum_)
        closepenality.reverse()
        closepenality.append(0)

        sum_=0
        print(closepenality)
        for i in range(len(customers)):
            if customers[i]=='N':
                sum_+=1
            closepenality[i+1]+=sum_
            openpenality.append(sum_)
        

        
        return closepenality.index(min(closepenality))



        