# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        return prev
        '''
        head of singly linked list
        - reverse it
        
        Initialize 3 pointers:
            prev = None
            current = head
            next_node/temp = None

        Travese the list:
            -store the next node
            -reverse the current node's pointer to prev
            -move all 1 step ahead
        
        Continue till curr = null and return prev

        prev = None, Curr = 1 -> 2 -> 3 -> 4 -> 5 -> None

        Steps:
            curr = 1
            prev = none
            next_node = 2

            curr = 2
            prev = 1
            next_node = 3

            curr = 3
            prev = 2
            next_node = 4

            curr = 4
            prev = 3
            next_node = 5

            curr = 5
            prev = 4
            next_node = None

            prev = 5

            return prev
        '''
        # prev = None
        # current = head

        # while current:
        #     next_node = current.next

        #     current.next = prev

        #     prev = current
        #     current = next_node

        # return prev

'''
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

1 -> 2 -> 3 -> 4 -> 5

prev = none, current = Node(1)

1st
next = Node(2)
current.
'''
