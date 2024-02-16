class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency=Counter(arr)

        arr.sort(key=lambda x:(frequency[x],x))
        uniqe=set()
        for i in range(k,len(arr)):
            uniqe.add(arr[i])
        
        
        return(len(uniqe))