class FrequencyTracker:

    def __init__(self):
        self.nas = defaultdict(int)
        self.freq=defaultdict(int)
        

    def add(self, number: int) -> None:
        self.nas[number]+=1
        self.freq[self.nas[number]]+=1
        if(self.freq[self.nas[number]-1]>0):
            self.freq[self.nas[number]-1]-=1
      
        

        

    def deleteOne(self, number: int) -> None:
        if self.nas[number]>0:
            self.nas[number]-=1
            self.freq[self.nas[number]]+=1
            if(self.freq[self.nas[number]+1]>0):
                self.freq[self.nas[number]+1]-=1

  
        
    def hasFrequency(self, frequency: int) -> bool:
        if(self.freq[frequency]>0):
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)