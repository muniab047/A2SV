class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=persons
        self.times=times
        self.winner=[]
        counter=defaultdict(int)
        win=-1

        for p in persons:
            counter[p]+=1
            if counter[p]>=counter[win]:
                win=p
            self.winner.append(win)
           

    def q(self, t: int) -> int:
        pos=bisect_right(self.times,t)-1
        return self.winner[pos]


        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)