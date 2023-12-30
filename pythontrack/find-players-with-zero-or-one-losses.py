class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=set()
        loser={}

        winans=[]
        losans=[]
        totans=[]

        for i in range(len(matches)):
            w,l= matches[i]

            winner.add(w)
            if l in loser.keys():
                loser[l]+=1

            else:
                loser[l]=1

        for num in winner:
            if not num in loser.keys():
                winans.append(num)

        for key in loser:
            if loser[key]==1:
                losans.append(key)

        winans.sort()
        losans.sort()
        totans.append(winans)
        totans.append(losans)

        return totans



        


        