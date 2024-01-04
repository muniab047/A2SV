class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index=0
        counter=0
        f=True

        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                if f:
                    counter+=1 
                    f=False

            if(i==0 and counter>0):
                return False
            if(counter>0):
                if arr[i]<=arr[i+1]:
                    counter+=1
      
        if counter!=1 :
            return False
        return True
        

        