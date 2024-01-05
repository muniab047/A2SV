class Solution:
    def smallestNumber(self, num: int) -> int:

        
        ans=0
        if num>=0:
            num=list(str(num))
            num.sort()
            for i in range(len(num)):
                if num[i]!='0':
                    temp=num[i]
                    num[i]='0'
                    num[0]=temp
                    break
            ans=''.join(num)
            ans=int(ans)
        else:
            num=num*-1
            num=list(str(num))
            num.sort(reverse=True)
            ans=''.join(num)
            ans=int(ans)*-1
        return ans


        