class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length=len(cardPoints)-k
        minSum=float('inf')
        summ=0
        left=0
        right=0
        win=0
        
        while right<=len(cardPoints):
            
            if win<length:
                if right<len(cardPoints):
                    summ+=cardPoints[right]
                right+=1
                win+=1
            else:
                minSum=min(minSum,summ)
                
                if right<len(cardPoints):
                    summ+=cardPoints[right]
                    summ-=cardPoints[left]
                left+=1
                right+=1
            print(summ, minSum,left,right)
        totalSum=sum(cardPoints)
        ans=totalSum-minSum
        return ans
