class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        ans=[]

        def generate(arr,idx):
            if idx==len(digits):
                ans.append(''.join(arr))
                return

            for i in range(len(mp[digits[idx]])):
                arr.append(mp[digits[idx]][i])
                generate(arr,idx+1)
                arr.pop()
        if len(digits)==0:
            return []
        generate([],0)
        return ans


        

        