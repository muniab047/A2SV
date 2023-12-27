class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even=[num for num in nums if num%2==0 ]
        summ=sum(even)
        ans=[]

        for j in range(len(queries)):
            v,i= queries[j]

            if(nums[i]%2==0 and v%2==0):
                summ+=v
            elif(nums[i]%2==0 and v%2!=0):
                summ-=nums[i]
            elif(nums[i]%2!=0 and v%2!=0):
                summ+=v+nums[i]
            nums[i]+=v

           


            ans.append(summ)

        return ans

        


        