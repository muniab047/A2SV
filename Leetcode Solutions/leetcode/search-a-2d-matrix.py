class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=[]
        for r in matrix:
            row.append(r[0])
        r= bisect_right(row, target)-1
        pos=bisect_right(matrix[r], target)-1

        if matrix[r][pos]==target:
            return True
        return False

        [1]
        