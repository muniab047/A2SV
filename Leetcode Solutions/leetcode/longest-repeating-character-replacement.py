class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter=defaultdict(int)
        ans=0

        left=0
        right=0

        def getmax():
            maxx=0
            for key in counter:
                maxx=max(maxx,counter[key])
            return maxx

        while right<=len(s) and left<len(s):
            length=right-left

            if length-getmax()<=k:
                if right<len(s):
                    counter[s[right]]+=1
                right+=1
            else:
                ans=max(ans,length-1)
                counter[s[left]]-=1
                left+=1
        ans=max(ans,right-left-1)
        return ans


            