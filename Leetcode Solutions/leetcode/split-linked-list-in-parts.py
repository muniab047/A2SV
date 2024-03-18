# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[]
        partition=k
        start=head
        end=head
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        while end:
            n=ceil(length/k)
            for i in range(n-1):
                if end:
                    end=end.next
                length-=1
            curr=end
            if end:
                end=end.next
            if curr:
                curr.next=None
            ans.append(start)
            start=end
            k-=1
            length-=1
        while len(ans)<partition:
            ans.append(None)
        
        return ans
            
            
        