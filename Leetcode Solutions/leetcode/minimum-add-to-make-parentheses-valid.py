class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        counter=0
        for p in s:
            if p=='(':
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                else:
                    counter+=1
        return len(stack)+counter