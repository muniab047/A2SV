class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        co=[0]*k
        ans=float('inf')


        def distribute(idx):
            nonlocal ans
            if max(co)>ans:
                return
            if idx==len(cookies):
                ans=min(ans,max(co))
                return
               
            for i in range(len(co)):
                if co[i]+cookies[idx] >ans or i>0 and co[i-1]==co[i]:
                    continue
                co[i]+=cookies[idx]
                distribute(idx+1)
                co[i]-=cookies[idx]
        distribute(0)
        return ans
        