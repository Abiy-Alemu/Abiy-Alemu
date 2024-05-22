# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        
        for i in range(n+1):
            if second is None:
                return None  
            second = second.next
        
       
        while second is not None:
            first = first.next
            second = second.next
        
        
        first.next = first.next.next
        
        return dummy.next
