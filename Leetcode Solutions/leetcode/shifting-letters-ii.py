class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums=[0 for i in range(len(s)+1)]
        ans=''
        
        for shift in shifts:
            start,end,direction=shift
            if direction==0:
                nums[start]-=1
                nums[end+1]+=1
            else:
                nums[start]+=1
                nums[end+1]-=1
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        nums.pop(-1)

        for i in range(len(nums)):          
            ans+=chr((ord(s[i])-97+nums[i])%26+97)           
        return ans

        