class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       uniqe=defaultdict(int)
       left=0
       right=0
       ans=0

       while right<len(fruits) and left<len(fruits):
           uniqe[fruits[right]]+=1
           right+=1
           while len(uniqe.keys())>2:
               uniqe[fruits[left]]-=1
               if uniqe[fruits[left]]==0:
                   uniqe.pop(fruits[left])
               left+=1
           ans=max(ans,right-left)
       ans=max(ans,right-left)
       return ans

       