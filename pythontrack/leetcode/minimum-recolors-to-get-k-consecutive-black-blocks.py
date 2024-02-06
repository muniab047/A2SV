class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        right=0
        counter=0
        minOperation=float('inf')
        length=0

        while right<=len(blocks):
            
            
            if length<k:
                if right <k:
                    if blocks[right]=='W':
                        counter+=1
                right+=1
                length+=1
            else:
                minOperation=min(minOperation,counter)
                if right<len(blocks):
                    if blocks[right]=='W':
                        counter+=1
                    
                if blocks[left]=='W':
                    counter-=1
                left+=1
                right+=1
            print(length,left,right,counter)
            
            
            
            
        if minOperation==float('inf'):
            return 0
        else: 
            return minOperation
                

        