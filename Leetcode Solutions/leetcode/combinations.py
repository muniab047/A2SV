class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans=[]
        def comb(arr,start):
            if len(arr)==k:
                ans.append(arr[:])
                return

            for i in range(start,n+1):
                arr.append(i)
                comb(arr,i+1)
                arr.pop()

        comb([], 1)
        return ans