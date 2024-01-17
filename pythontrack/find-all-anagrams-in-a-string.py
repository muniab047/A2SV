class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pdic=defaultdict(int)
        sdic=defaultdict(int)
        ans=[]
        f=True
        start=0

        for char in p:
            pdic[char]+=1
        for i in range(len(s)):
            if i<len(p):
                sdic[s[i]]+=1

            elif i>=len(p):
                sdic[s[i]]+=1
                sdic[s[start]]-=1
                if sdic[s[start]] <1:
                    sdic.pop(s[start])
                start+=1

            if sdic==pdic:
                ans.append(start)         
        return ans


                
               