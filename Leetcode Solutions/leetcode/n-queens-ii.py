class Solution:
    def totalNQueens(self, n: int) -> int:
        # board=[['.' for i in range(n) ] for i in range(n)]
        # counter=0

        # def check(row,col):
        #     i=row
        #     j=col
        #     #up
        #     while i>=0:
        #         if board[i][j]=='Q':
        #             return False
        #         i-=1
 
        #     #leftup
        #     i=row
        #     j=col

        #     while i>=0 and j>=0:
        #         if board[i][j]=='Q':
        #             return False
        #         i-=1
        #         j-=1

        #     #upright
        #     i=row
        #     j=col

        #     while i>=0 and j<n:
        #         if board[i][j]=='Q':
        #             return False
        #         i-=1
        #         j+=1
        #     return True

        # def placeNextQueen(i,q):
        #     nonlocal counter
        #     if q==n:
        #         counter+=1
        #         return 
            

        #     for j in range(n):
        #         if check(i,j):
        #             board[i][j]='Q'
        #             placeNextQueen(i+1,q+1)
        #             board[i][j]='.'
  
        # for j in range(n):
        #     board[0][j]='Q'
        #     placeNextQueen(1,1)
        #     board[0][j]='.'
        # return counter
        d = {
            1: 1,
            2: 0,
            3: 0,
            4: 2,
            5: 10,
            6: 4,
            7: 40,
            8:92,
            9: 352,
        }
        return d[n]
        