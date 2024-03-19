class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque()
        D=deque()

        for i in range(len(senate)):
            if senate[i]=='R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            if R[0]<D[0]:
                D.popleft()
                R.append(R[0]+len(senate))
                R.popleft()
            else:
                R.popleft()
                D.append(D[0]+len(senate))
                D.popleft()
        if R:
            return 'Radiant'
        return 'Dire'




        