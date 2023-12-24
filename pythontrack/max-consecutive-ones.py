class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        start=0
        
        ls=[]

        while(start< len(nums)):
            if(nums[start]==1):
                counter+=1
                
            else:
                ls.append(counter)
                counter=0

        

            start+=1

        ls.append(counter)

        return max(ls)



        