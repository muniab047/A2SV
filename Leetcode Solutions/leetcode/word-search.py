class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(i,j, ind):
            if ind==len(word):
                return True
            if i== len(board) or j==len(board[0]) or i <0 or j<0:
                return False
            if board[i][j]==word[ind]:
                value=board[i][j]
                board[i][j]=''
                if check(i+1,j,ind+1):
                    return True
                if check(i,j+1,ind+1):
                    return True
                if check(i-1,j,ind+1):
                    return True
                if check(i,j-1,ind+1):
                    return True
                board[i][j]=value

                
                

            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i,j,0):
                    return True


        return False




        


        