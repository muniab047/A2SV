class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans=[]
        max_=0

        def split(idx):
            nonlocal max_
            if idx==len(s):
                if len(set(ans))==len(ans):
                    max_=max(max_,len(ans))
                return


            for i in range(idx,len(s)):
                ans.append(s[idx:i+1])
                split(i+1)
                ans.pop()
        split(0)
        return max_






