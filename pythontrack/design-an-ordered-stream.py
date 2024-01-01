class OrderedStream:

    def __init__(self, n: int):
        self.ptr=1
        self.dic={}
        self.ans=[]

        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey]=value
        self.ans=[]
        while(self.ptr in self.dic.keys()):
            self.ans.append(self.dic[self.ptr])
            self.ptr+=1

        return self.ans


        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)