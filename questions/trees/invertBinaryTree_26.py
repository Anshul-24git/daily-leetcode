# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()

            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
        '''
        Given root
        Invert the tree : swap the L & R child of every node
        return it's root

        Brute force (recursive):
            Recursively
                traverse each node
                swap the L & R of each node
                Recursively invert L & R subtrees

        Optimal approach (iterative):

            Queue to store node
            swap its children
                add it to queue
            continue and return

        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]

        root = [4,2,7,1,3,6,9]
        queue = [4], current = 4
        L = 7, R = 2 -> Swap them
        queue = [7, 2]
        Process 7 :
            L = 9, R = 6, queue = [2, 9, 6]
        Process 2:
            L = 3, R = 1, queue = [9, 6, 3, 1]
        Process children:
            9, 6, 3, 1
        Result : inverted tree
        [4,7,2,9,6,3,1]
        '''

        # if not root:
        #     return None

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)

        # self.invertTree(root.right)

        # return root        
        
'''
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

1. Start with root = 4
2. Swap children: left - 7 ; right - 2
3. Recrsively call invertTree(7)
'''
