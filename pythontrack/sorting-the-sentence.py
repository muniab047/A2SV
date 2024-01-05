class Solution:
    def sortSentence(self, s: str) -> str:
        dic=defaultdict(int)
        ans=''
        sl=s.split()
        for s in sl:
            dic[int(s[-1])]=s[:len(s)-1]

        ans+=dic[1]
        for i in range(2,len(sl)+1):
            ans+=f' {dic[i]}'
        return ans

        

        
        