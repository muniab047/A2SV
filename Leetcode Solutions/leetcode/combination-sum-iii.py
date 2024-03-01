class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:


        ans=[]
        arr=[]

        def combine(idx):
            if sum(arr)==n and len(arr)==k:
                ans.append(arr[:])
                return
            if sum(arr)>n:
                return

            for i in range(idx,10):
                arr.append(i)
                combine(i+1)
                arr.pop()
        combine(1)
        return ans
            


