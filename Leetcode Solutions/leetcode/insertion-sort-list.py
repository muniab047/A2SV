# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        while head:
            temp=head
            head=head.next
            temp2=dummy
            while temp2.next and (temp2.next.val<temp.val):
                temp2=temp2.next
            if temp2.next:
                temp.next=temp2.next
                temp2.next=temp
            else:
                temp.next=None
                temp2.next=temp
        head=dummy.next
        return head
        