class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if p=='(' or p=='[' or p=='{':
                stack.append(p)
            else:
                if stack:
                    if p==')':
                        if stack[-1]=='(':
                            stack.pop()
                            continue
                    elif p==']':
                        if stack[-1]=='[':
                            stack.pop()
                            continue
                    elif p=='}':
                        if stack[-1]=='{':
                            stack.pop()
                            continue
                return False
        if stack:
            return False
        return True
                
        