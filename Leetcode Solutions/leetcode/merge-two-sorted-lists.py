# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
        

        new_head = None
        temp = new_head
        while list1 and list2 :
            if list1.val < list2.val:
                if not new_head:
                    new_head = list1
                    list1 = list1.next
                    new_head.next = None
                    temp = new_head
                else:
                    temp1 = list1
                    list1 = list1.next
                    temp1.next = None
                    temp.next = temp1
                    temp = temp.next
            else:
                if not new_head:
                    new_head = list2
                    list2 = list2.next
                    new_head.next = None
                    temp = new_head
                else:
                    temp1 = list2
                    list2 = list2.next
                    temp1.next = None
                    temp.next = temp1
                    temp = temp.next

        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return new_head


            