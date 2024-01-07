class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr1=0
        ptr2=0
        counter=0

        g.sort()
        s.sort()
        max=0

        while ptr1<len(g) and ptr2<len(s):
            if g[ptr1]<=s[ptr2]:
                counter+=1
                ptr1+=1
                ptr2+=1
            elif g[ptr1]>s[ptr2]:
                ptr2+=1
        return counter

        
        