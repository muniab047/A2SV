class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        counter=0
        while(i<len(costs) and coins>0):
            coins-=costs[i]
            if(coins<0):
                break
            counter+=1
            i+=1
        return counter

        