# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val<=list2.val:
            head=list1
            temp2=list2
        else:
            head=list2
            temp2=list1
        temp=head
        while temp and temp2 :
            if temp.next and temp2 and temp.next.val<temp2.val :
                temp=temp.next
            else:
                curr=temp2
                temp2=temp2.next
                curr.next=temp.next
                temp.next=curr
                temp=temp.next
       

        
        return head


            