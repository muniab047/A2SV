class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i= min(start,destination)
        j= max(start,destination)

        ans1=sum(distance[i:j])
        ans2=sum(distance)-ans1
        return(min(ans1,ans2))
        
        