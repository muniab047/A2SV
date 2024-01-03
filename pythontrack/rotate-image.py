class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:]= zip(*matrix)
        matrix[:]=[list(l) for l in matrix]
        for i in range(len(matrix)):
            matrix[i]=list(reversed(matrix[i]))
        print(matrix)
        
        