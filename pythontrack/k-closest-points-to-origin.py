class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic=defaultdict(list)
        ans=[]
        for point in points:
            x,y=point
            dic[x**2+y**2].append(point)

        dic=dict(sorted(dic.items()))

        for key in dic:
            for ele in dic[key]:
                ans.append(ele)
                k-=1
            if k==0:
                break
        return ans

        