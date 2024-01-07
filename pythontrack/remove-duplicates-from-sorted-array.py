class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr=0

        for num in nums:
            if ptr==0 or num>nums[ptr-1]:
                nums[ptr]=num
                ptr+=1

        
        return ptr

        