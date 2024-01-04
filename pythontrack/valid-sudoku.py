class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardT=list(zip(*board))
        boardsq=[]
        
        for i in range (0,9,3):
            
            for j in range (0,9,3):
                s=[]
                s.append(board[i][j])
                s.append(board[i+1][j])
                s.append(board[i+2][j])
                s.append(board[i][j+1])
                s.append(board[i+1][j+1])
                s.append(board[i+2][j+1])
                s.append(board[i][j+2])
                s.append(board[i+1][j+2])
                s.append(board[i+2][j+2])
                boardsq.append(s)
        # print(board)
        # print(boardT)
        # print(boardsq)

        for i in range(9):
            if(i==0 or i==1 or i==2):k=-1
            elif(i==3 or i==4 or i==5):k=2
            else:k=5
            
            

            for j in range(9):
                num=board[i][j]
                if(j%3==0):
                    k+=1
               
                
                if(num!='.'):
                    print(board[i],boardsq[k],boardT[j])
                    if(board[i].count(num)>1 or boardsq[k].count(num)> 1 or boardT[j].count(num)>1):
                        return False
                

        return True

            
                
        