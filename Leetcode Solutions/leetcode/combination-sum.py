class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        def combine(idx, sum_):
            if sum_==target:
                ans.append(arr[:])
                return
            if sum_>target:
                return

            for i in range(idx, len(candidates)):
                sum_+=candidates[i]
                arr.append(candidates[i])
                combine(i, sum_)
                sum_-=candidates[i]
                arr.pop()
        
        combine(0, 0)
        return ans

        