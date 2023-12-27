class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start=0
        end=start+1
        counter=1
        nums=list(set(nums))
        nums.sort()
        
        print(nums)
        ans=[]

        if nums==[]:
            return 0

        while(end<len(nums)):
            if(nums[end]-nums[start]==1):
                counter+=1
               
                
            else:
                
                ans.append(counter)
                counter=1
            start+=1
            end+=1

        ans.append(counter)


        

        return max(ans)

        