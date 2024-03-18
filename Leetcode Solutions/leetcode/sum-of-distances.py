class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix_index=defaultdict(lambda: [0])
        index=defaultdict(int)
        ans=[]
        for i in range(len(nums)):
            prefix_index[nums[i]].append(prefix_index[nums[i]][-1]+i)
        
        for i in range(len(nums)):
           dicindex=index[nums[i]]
           left=(i*dicindex)-prefix_index[nums[i]][dicindex]
           postfix_index=prefix_index[nums[i]][-1]-prefix_index[nums[i]][dicindex+1]
           right=postfix_index-(i*(len(prefix_index[nums[i]])-dicindex-2))

           index[nums[i]]+=1
           ans.append(left+right)

        return ans

            


        


        