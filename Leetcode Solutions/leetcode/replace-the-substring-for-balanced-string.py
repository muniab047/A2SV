class Solution:
    def balancedString(self, s: str) -> int:
        counter=Counter(s)

        left=0
        right=0
        ans=float('inf')
        target=len(s)//4

        while right<=len(s) and left<len(s):    
            for k in counter:
                if counter[k]>target:
                    break
            else:
                ans=min(ans,right-left)
                counter[s[left]]+=1
                left+=1
                continue
            if right<len(s):  
                counter[s[right]]-=1
            right+=1
        

        return ans

            

        