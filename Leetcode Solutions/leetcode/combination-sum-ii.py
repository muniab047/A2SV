class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        while candidates and candidates[-1]>target:
            candidates.pop()
        ans = []
        path = []
        def combine(index,sm):
            if sm>target:
                return 
            if sm==target:               
                ans.append(path[:])
                return
                       
            seen=set()
            for i in range(index,len(candidates)):
                if candidates[i] not in seen:
                    sm+=candidates[i]
                    path.append(candidates[i])
                    combine(i+1,sm)
                    sm-=path.pop()
                    seen.add(candidates[i])
        combine(0, 0)
        return ans
