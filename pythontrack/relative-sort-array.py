class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=defaultdict(lambda:float('inf'))
        for i in range(len(arr2)):
            dic[arr2[i]]=i

        arr3=[]
        i=0

        while i<len(arr1):
            if arr1[i] not in arr2:
                arr3.append(arr1[i])
                arr1.remove(arr1[i])
                i-=1
            i+=1
            

        for i in range(len(arr1)):
            for j in range(len(arr1)):
                if dic[arr1[i]]< dic[arr1[j]]:
                    arr1[i],arr1[j]= arr1[j],arr1[i]



        arr3.sort()
        arr1.extend(arr3)
        


        return arr1


        