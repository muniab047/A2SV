class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter=Counter(s)
        ans=0
        maxOdd=0
        f=False
        for key in counter:
            if counter[key]%2==0:
                ans+=counter[key]
            else:
                ans+=counter[key]-1
                f=True
        if f:
            return ans+1
        return ans
               
        