class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        mptr=1
        bptr=len(piles)-1
        counter=0

        while(mptr<bptr):
            counter+=piles[mptr]
            mptr+=2
            bptr-=1

        return counter


        