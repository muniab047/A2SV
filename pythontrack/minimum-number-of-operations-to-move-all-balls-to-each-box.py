class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            moves=0
            for j in range(len(boxes)):
                
                if(boxes[j]!= '0'):
                    moves+=abs(i-j)
            ans.append(moves)

        return ans



        