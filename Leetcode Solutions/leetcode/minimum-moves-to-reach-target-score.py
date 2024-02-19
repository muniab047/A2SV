class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter=0
        moves=target
        while moves>1 and maxDoubles>0:
            if moves%2==0:
                counter+=1
            else:
                counter+=2
            moves//=2
            maxDoubles-=1
           
            
        return counter+(moves-1)
            
        