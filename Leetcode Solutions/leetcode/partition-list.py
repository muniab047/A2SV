# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy1=ListNode(val=0)
        dummy2=ListNode(val=0)
        temp1=dummy1
        temp2=dummy2

        temp=head
        while(temp):
            if temp.val<x:
                temp1.next=temp
                temp=temp.next
                temp1=temp1.next
                temp1.next=None
            else:
                temp2.next=temp
                temp=temp.next
                temp2=temp2.next
                temp2.next=None 
        temp1.next=dummy2.next
        head=dummy1.next
        return head
          
            
        