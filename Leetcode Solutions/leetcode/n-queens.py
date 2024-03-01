class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for i in range(n) ] for i in range(n)]
        ans=[]

        def check(row,col):
            i=row
            j=col
            #up
            while i>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                    
            #leftup
            i=row
            j=col

            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1

            #upright
            i=row
            j=col

            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True

        def placeNextQueen(i,q):
            if q==n:
                ans.append([''.join(b) for b in board])
                return 
            

            for j in range(n):
                if check(i,j):
                    board[i][j]='Q'
                    placeNextQueen(i+1,q+1)
                    board[i][j]='.'
  
        for j in range(n):
            board[0][j]='Q'
            placeNextQueen(1,1)
            board[0][j]='.'
        return ans

           

                

        