class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        arr=[]
        left=0
        right=0
        
        def generate():
            nonlocal left,right
            if left==right ==n:
                ans.append(''.join(arr))
                return
            if left<right:
                return           

            if left<n:
                arr.append('(')
                left+=1
                generate()
                arr.pop()
                left-=1
            arr.append(')')
            right+=1
            generate()
            arr.pop()
            right-=1
        generate()
        return ans