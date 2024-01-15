class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]

        while len(arr)>1:
            maxx=max(arr)
            index=arr.index(maxx)+1
            arr2=list(reversed(arr[:index]))
            arr2=arr2+arr[index:]
            arr=arr2
            ans.append(index)
            arr.reverse()
            ans.append(len(arr))
            arr.pop()

        return ans
            


        