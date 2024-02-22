class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex=defaultdict(int)
        ans=[]
        for i in range(len(s)):
            lastindex[s[i]]=i
        anchor=j=0

        for i in range(len(s)):
            j=max(j,lastindex[s[i]])
            if j==i:
                ans.append(i-anchor+1)
                anchor=i+1
        return ans
            

        
        