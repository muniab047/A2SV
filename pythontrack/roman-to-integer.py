class Solution:
    def romanToInt(self, s: str) -> int:

        symbol={'I':1, 'V':5, 'X':10, 'L':50, 'C':100 , 'D': 500, 'M':1000}

        i=0
        num=0
        while(i<len(s)):
            if(i+1<len(s) and symbol[s[i]] >=symbol [s[i+1]]):
                num+=symbol[s[i]]
                i+=1
            elif(i+1==len(s)):
                num+=symbol[s[i]]
                break
            else:
                num+= symbol[s[i+1]]-symbol[s[i]]
                i+=2

        return num



        
        