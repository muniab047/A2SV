# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev=None
        fast=head
        slow=head

        while fast.next and fast.next.next:
            fast=fast.next.next
            temp=slow 
            slow=slow.next          
            temp.next=prev
            prev=temp
        if fast.next:
            temp=slow 
            slow=slow.next          
            temp.next=prev
            prev=temp
        else:
            slow=slow.next

        left=prev
        right=slow      
        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
            
        return True

        
        
            

            

        