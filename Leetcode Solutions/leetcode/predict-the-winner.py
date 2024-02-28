class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def isplayer1win(start,end,score1,score2,turn):
            if start>end:
                return score1>=score2
            if turn==1:
                choicestart= isplayer1win(start+1,end,score1+nums[start],score2,turn=2)
                if choicestart:
                    return True
                choiceend=isplayer1win(start,end-1,score1+nums[end],score2,turn=2)
                if choiceend:
                    return True 


                return False


            elif turn==2:
                choicestart= isplayer1win(start+1,end,score1,score2+nums[start],turn=1)
              
                choiceend=isplayer1win(start,end-1,score1,score2+nums[end],turn=1)
                if choicestart and choiceend:
                    return True

                return False
            

        return isplayer1win(0,len(nums)-1,0,0,turn=1)
