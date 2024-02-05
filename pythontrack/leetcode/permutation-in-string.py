class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter=defaultdict(int)
        s2Counter=defaultdict(int)
        for char in s1:
            s1Counter[char]+=1
        left=0
        right=0
        ans=''
        i=0

        while right<len(s2):
            if i<len(s1):
                s2Counter[s2[right]]+=1
                i+=1
                right+=1
            else:
                s2Counter[s2[left]]-=1
                s2Counter[s2[right]]+=1

                if s2Counter[s2[left]]==0:
                    s2Counter.pop(s2[left])
                right+=1
                left+=1
            

            if s2Counter==s1Counter:
                return True

        return False