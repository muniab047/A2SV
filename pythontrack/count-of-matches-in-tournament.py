class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        team=n
        summ=0

        while(team>1):
            if(team%2==0):
                matches=team//2
                team=team//2
                
            else:
                matches=(team-1)//2
                team=((team-1)//2)+1
                


            summ+=matches

        return summ
        