class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dic=defaultdict(lambda:-1)
        stack=[]
        ans=[]
        i=0

        while i!=2*len(nums):
            while stack and stack[-1][0]<nums[i%len(nums)]:
                dic[stack[-1]]=nums[i%len(nums)]
                stack.pop()
            stack.append((nums[i%len(nums)],i%len(nums)))
            i+=1
        for i in range(len(nums)):
            ans.append(dic[(nums[i%len(nums)],i%len(nums))])
       
        return ans

            

        