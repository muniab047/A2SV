class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps=[]
        
        cap=capacity

        for i in range(len(plants)):
            step=0
            if plants[i]<=cap:
                step+=1
                cap-=plants[i]
            else:
                step+= 2*i+1
                cap=capacity
                cap-=plants[i]

            steps.append(step)

        return sum(steps)

        

        

        