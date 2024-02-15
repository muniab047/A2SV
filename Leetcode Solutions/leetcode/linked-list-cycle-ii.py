# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        fast=head
        slow=head
        i=0



        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                temp=head
                while(temp!= slow):
                    temp=temp.next
                    slow=slow.next
                    i+=1
                return temp
        return None
        