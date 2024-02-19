class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        counter=[0 for i in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                counter[stack[-1][0]]=i-stack[-1][0]
                stack.pop()

            stack.append((i,temperatures[i]))

        
        

        return counter

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in Solution().dailyTemperatures(case)])}]\n")
exit()
