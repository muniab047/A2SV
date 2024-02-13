# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        temp=head
        if not head:
            return None
        while temp:
            length+=1
            temp=temp.next
        rotate=length-(k%length)-1
        temp=head
        newhead=head
        

        while temp : 
            if rotate==0:
                newhead=temp.next
                temp.next=None
                temp=newhead
                
            if temp and temp.next==None:
                temp.next=head
                head=newhead
                break
            if rotate!=0:
                temp=temp.next
        
            rotate-=1

        return head