class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

       
        li=set()

        for i in range (len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                li.add(j)

        for k in range(left, right+1):
            if k not in li:
                return False

        return True

        

        