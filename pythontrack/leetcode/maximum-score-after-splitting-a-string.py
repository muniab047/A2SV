class Solution:
    def maxScore(self, s: str) -> int:
        prefixSumLeft = [1-int(s[0])]
        s = [int(i) for i in s]
        ones = sum(s)
        ones-=s[0]
        prefixSumRight=[ones]
        mx = 0
        for i in range(1,len(s)-1):
            mx = max(mx,prefixSumLeft[i-1]+prefixSumRight[i-1])
            prefixSumLeft.append(prefixSumLeft[-1]+(1-s[i]))
            if s[i]==1:
                ones-=s[i]
            prefixSumRight.append(ones)
        mx = max(mx,prefixSumLeft[-1]+prefixSumRight[-1])
        return mx
        
        