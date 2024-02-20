class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2,n,pow(10,9)+7 )-2)%(pow(10,9)+7)


# with open('user.out', 'w') as f:
#     for case in map(loads, stdin):
#         f.write(f"[{','.join([str(x) for x in Solution().dailyTemperatures(case)])}]\n")
# exit()
       