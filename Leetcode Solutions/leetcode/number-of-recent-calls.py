class RecentCounter:

    def __init__(self):
        self.queues=[]
        
        

    def ping(self, t: int) -> int:
        self.queues.append(t)
        counter=0
        for queue in self.queues:
            if queue >=t-3000 and queue<=t:
                counter+=1
        return counter


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)