class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxx=0

        for i in range(1,len(points)):
            x1,y1=points[i]
            x2,y2=points[i-1]
            if x1-x2>maxx:
                maxx=x1-x2
        return maxx
        