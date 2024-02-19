class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        counter=1
        intersection=points[0]
        for i in range(1,len(points)):
            x1,x2=points[i]
            a1,a2=intersection
            if x1<=a2:
                intersection=[x1,min(a2,x2)]
            else:
                counter+=1
                intersection=[x1,x2]

        return counter


