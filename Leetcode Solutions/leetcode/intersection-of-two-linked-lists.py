# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempa=headA
        tempb=headB

        lengtha=0
        lengthb=0

        while tempa or tempb:
            if tempa:
                lengtha+=1
                tempa=tempa.next
            if tempb:
                lengthb+=1
                tempb=tempb.next
        diff=abs(lengtha-lengthb)

        
        for i in range(diff):
            if lengtha>lengthb:
                headA=headA.next
            else:
                headB=headB.next
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next

    

        


        