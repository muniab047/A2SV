class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        li=list(palindrome)
        ans=''
        j=1
        if len(li)==1:
            return ''
        for i in range(len(li)//2):
            if li[i]>'a':
                li[i]='a'
                ans=''.join(li)
                return ans
        li[-1]='b'
        ans=''.join(li)
        return ans


        