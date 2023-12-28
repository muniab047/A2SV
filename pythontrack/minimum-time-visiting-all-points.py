class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=[]
        for i in range(1,len(points)):
            x1, y1= points[i]
            x2, y2= points[i-1]
            xd=abs(x2-x1)
            yd=abs(y2-y1)
            ans.append(max(xd,yd))

        return sum(ans)

        