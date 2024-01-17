class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        ans=[]

        ptr1=0
        ptr2=0

        while ptr1<len(processorTime):
            x=processorTime[ptr1]
            ans.append(max(x+tasks[ptr2],x+tasks[ptr2+1],x+tasks[ptr2+2],x+tasks[ptr2+3]))
            ptr1+=1
            ptr2+=4

        return max(ans)
        