# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        #finding middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #spilt the list
        second_half = slow.next
        slow.next = None

        #reverse
        prev = None
        curr = second_half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #merge
        first_half = head
        second_half = prev

        while second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next
        '''
        1 -> 2 -> 3 -> 4 -> 5 -> null
                  s
                             f
        1 -> 2 
        4 -> 3

        Middle:
            slow = 1, fast = 1, prev = None
            slow = 2, fast = 3, prev = 1
            slow = 3, fast = 5, prev = 2
            fast.next = None -> stop
            Split : 1 -> 2 and  3 -> 4 -> 5

        Reverse:
            3 -> 4 -> 5 becomes 5 -> 4 -> 3

        Merge:

            first = 1, second = 5 : 1 -> 5, temp1 = 2, temp2 = 4
            first = 2, second = 4 : 1 -> 5 -> 2 -> 4, temp1 = None, temp2 = 3
            first = None, second = 3 : 1 -> 5 -> 2 -> 4 -> 3

        Final list : 1 -> 5 -> 2 -> 4 -> 3
        
        Big O (complexities):
            Time: O(n)
            Space : O(1)
        '''
