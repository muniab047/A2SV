class Solution:
    def minimumSteps(self, s: str) -> int:
        pos=0
        ans=0

        for i in range(len(s)):
            if s[i]=='0':
                ans+=(i-pos)
                pos+=1
        return ans
