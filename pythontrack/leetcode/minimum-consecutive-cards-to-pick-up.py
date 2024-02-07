class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0
        right=0
        noOfMatches=0
        cardCounter=defaultdict(int)
        minLength=float('inf')
        length=0

        while left<len(cards) and right<len(cards):
            if right<len(cards) and cardCounter[cards[right]]<1:
                cardCounter[cards[right]]+=1
                if right<len(cards):
                    right+=1
            else:
                length=right-left+1
                minLength=min(minLength,length)
                cardCounter[cards[left]]-=1
                left+=1

        if minLength==float('inf'):
            return -1
        else:
            return minLength


        