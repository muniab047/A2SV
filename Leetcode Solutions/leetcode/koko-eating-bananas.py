class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        higher = max(piles)
        best=higher
        def getHour(speed):
            hour=0
            for i in range(len(piles)):
                hour += ceil(piles[i]/speed)
            return hour
    

        while lower<=higher:
            mid = lower+ (higher-lower)//2

            currentHour=getHour(mid)
            if currentHour <= h:
                higher=mid-1
                best=mid
            else:
                lower=mid+1
        
        return best