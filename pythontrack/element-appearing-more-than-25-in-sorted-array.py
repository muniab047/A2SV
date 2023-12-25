class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        occ=len(arr)/4

        for i in range(len(arr)):
            if arr.count(arr[i])>occ and len(arr)>1:
                return arr[i]
            elif(len(arr)==1):
                return arr[0]

        