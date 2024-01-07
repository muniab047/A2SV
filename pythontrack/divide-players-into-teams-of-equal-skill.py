class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start=0
        end=len(skill)-1
        summ=0

        

        while start+1<end-1:
            if skill[start]+skill[end]!=skill[start+1]+skill[end-1]:
                return -1
            else:
                summ+=(skill[start]*skill[end])
                print(summ)
                start+=1
                end-=1
        summ+=(skill[start]*skill[end])
        return summ

        