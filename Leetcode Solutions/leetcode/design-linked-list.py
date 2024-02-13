class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        
        
        
class MyLinkedList:

    def __init__(self):
        self.dummy=Node(-1)
        self.head=None

    def get(self, index: int) -> int:
        temp=self.dummy
        while temp and temp.next and index>=0:
            temp=temp.next
            index-=1
        if index>=0:
            return -1       
        return temp.val
       
    def addAtHead(self, val: int) -> None:
        temp=self.dummy
        node=Node(val)       
        if temp.next:  
            node.next=temp.next
        temp.next=node
        self.head=temp.next      

    def addAtTail(self, val: int) -> None:
        temp=self.dummy
        while temp and temp.next:
            temp=temp.next
        node=Node(val)
        temp.next=node
        node.next=None

    def addAtIndex(self, index: int, val: int) -> None:
        temp=self.dummy
        while index>0 and temp and temp.next:
            temp=temp.next
            index-=1
        if index<=0:
            node=Node(val)
            node.next=temp.next
            temp.next=node 
              

    def deleteAtIndex(self, index: int) -> None:
        temp=self.dummy
        while temp and temp.next and index>0:
            temp=temp.next
            index-=1
        if temp.next and temp.next.next:
            
            temp.next=temp.next.next
        else:
            temp.next=None
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)