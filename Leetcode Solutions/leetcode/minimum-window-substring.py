class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        right=0

        tcounter=Counter(t)
        scounter=Counter()
        ans=[0,float('inf')]


        def check():
            for k in tcounter:
                if scounter[k]<tcounter[k]:
                    return True
            return False

        while right<=len(s) and left<len(s):

            if check():
                if right<len(s) and s[right] in tcounter:
                    scounter[s[right]]+=1
                right+=1
            else:
                if ans[1]-ans[0]> right-left:
                    ans=[left,right]
                if s[left] in tcounter:
                    scounter[s[left]]-=1
                left+=1
            
        try:
            return s[ans[0]:ans[1]]
        except:
            return ''






        