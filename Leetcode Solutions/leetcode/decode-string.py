class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            ans=''
            num=''
            while i<len(s):
                if s[i].isdigit():                
                    num+=s[i]
                elif s[i].isalpha():
                    ans+=s[i]
                elif s[i]=='[':
                    q=decode(i+1)
                    ans+=int(num)*q[0]
                    i=q[1]
                    num=''
                elif s[i]==']':
                    return (ans, i)
                i+=1


            return (ans,-1)
        
        return decode(0)[0]

