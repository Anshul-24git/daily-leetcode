# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
        '''
        list 1 & list 2
        merge them into 1 sorted list
        return head of merged list
        slice together the 2 lists for the merged one
        
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        list1 : 1 -> 2 -> 4
        list2: 1 -> 3 -> 4

        Step 1:
            dummy -> 1 vs 1, take list1 value
        Step 2:
            dummy -> 1 | 2 vs 1, take 1 from l2
        Step 3:
            dummy -> 1 -> 1
        '''
