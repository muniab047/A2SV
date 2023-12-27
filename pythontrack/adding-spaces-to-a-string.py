class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        start=0
        ans=[]

        for i in range (len(spaces)):
            sl=s[start:spaces[i]]
            ans.append(sl)
            start=spaces[i]
        sl=s[spaces[-1]:]
        ans.append(sl)
        ans2=' '.join(ans)

        return ans2
        