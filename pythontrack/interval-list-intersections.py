class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        lis = []
        for x,y in firstList:
            for i, j in secondList:
                if x >= i and x<=j and y <= j and y >=i:
                    lis.append([x, y])
                elif x >= i and x<=j and j<=y and j>=x:
                    lis.append([x,j])
                elif i >=x and i<=y and y <= j and y >=i:
                    lis.append([i,y])
                elif i >=x and i<=y and j<=y and j>=x:
                    lis.append([i,j])
        return lis
        