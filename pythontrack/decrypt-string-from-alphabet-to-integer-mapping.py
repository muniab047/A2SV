class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        ans=''
        while(i+1<=len(s)):
            if(i+2<=len(s)-1 and s[i+2]!='#'):
                ans+=chr(96+int(s[i]))
                i+=1

            elif(len(s)-1-i<2):
                ans+=chr(96+int(s[i]))

                
                i+=1
            else:
                num=int(s[i]+s[i+1])
                ans+=chr(96+num)
                i+=3

        return ans



        