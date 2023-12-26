class Solution:
    def printVertically(self, s: str) -> List[str]:
        li=s.split()
        ansli=[]
        for j in range(len(max(li, key=len))):
            ans=''
            for i in range(len(li)):
                if(j<len(li[i])):
                    ans+=li[i][j]
                else:
                    ans+=" "

            # ans.rstrip()
            # print(ans)

            ansli.append(ans)

        return [i.rstrip() for i in ansli]

            
            
        