class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        double=[]
        good=[]
        for i in range(len(fronts)):
            if(fronts[i]==backs[i]):
                double.append(fronts[i])
            
        for j in range(len(fronts)):
            if fronts[j] not in double:
                good.append(fronts[j])
                
            if backs[j] not in double:
                good.append(backs[j])

      
        return min(good, default=0)


        


        
   
        
                

        
                

        