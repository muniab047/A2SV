class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=defaultdict(int)
        maxx=0

        for booking in bookings:
            first, last,seat=booking
            res[first]+=seat
            res[last+1]-=seat
            maxx=max(maxx,last+1)

        prefix=[0]
        length=len(res)
        

        for i in range(1,n+1):
            prefix.append(prefix[i-1]+res[i])

        prefix.pop(0)



        

        
        return prefix
       
        

        