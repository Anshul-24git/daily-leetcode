# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        slow = head
        fast = head

        while fast and fast.next:
            #move slow pointer once
            slow = slow.next
            #move fast pointer twice
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        '''
        Given:
            head
            next
            pos
        O/p:
            true or false | cycle detection

        head = [3,2,0,-4], pos = 1
        List : 3 -> 2 -> 0 -> -4
        '''
        
