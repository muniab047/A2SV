class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        for i in range(len(tickets)):
            if i <=k:
                time+=(min(tickets[i],tickets[k]))
            else:
                value=min(tickets[i],tickets[k])
                if value>=tickets[k]:
                    time+=value-1
                else:
                    time+=value
    
        return time
       
        