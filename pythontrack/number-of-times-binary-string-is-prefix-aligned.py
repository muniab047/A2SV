class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        counter=0
       
        sumindex=0
        sumvalue=0

        for i in range(len(flips)):
            sumindex+=i+1
            sumvalue+=flips[i]
            print(sumindex,sumvalue)
            if(sumindex==sumvalue):
                counter+=1

        return counter



        