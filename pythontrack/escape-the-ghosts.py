class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_step=abs(target[1])+abs(target[0])

        for i in range(len(ghosts)):
            x,y=ghosts[i]
            ghost_step=abs(x-target[0])+abs(y-target[1])

            if(ghost_step<=my_step):
                print(ghosts[i])
                return False

            

        return True