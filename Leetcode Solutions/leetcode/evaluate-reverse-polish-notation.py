class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=='+' or token=='-' or token=='*' or token=='/':
                a=stack.pop()
                b=stack.pop()
                c=str(int(eval(b+token+a)))
                stack.append(c)
            else:
                stack.append(token)

        ans=int(stack[0])

        return ans

        