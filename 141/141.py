# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if(not head or not head.next):
            return None
        p1 = head
        p2 = head.next

        while(p2 != None and p2.next != None):
            if(p1 == p2):
                return True
            else:
                p1 = p1.next
                p2 = p2.next.next
        
        return False


