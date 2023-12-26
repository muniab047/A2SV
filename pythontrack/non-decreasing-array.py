class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        counter=0
        index=0

        for i in range (1,len(nums)):
           
           if(nums[i]<nums[i-1]):
               counter+=1
               index=i

        if(counter>1 ):
            return False

        else:
            left=nums.copy()
            right=nums.copy()
            right.pop(index)
            left.pop(index-1)
            if(left== sorted(left) or right==sorted(right)):
                return True
            else:
                return False
