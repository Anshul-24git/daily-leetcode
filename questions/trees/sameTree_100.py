# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same

        
        '''
        p & q
        same or not
        o/p : T/F

        Input: p = [1,2,3], q = [1,2,3]

        Step 1:
            p = 1, q = 1
            compare root: (1 == 1)
            looks good - move left

        Step 2:
            p = 2, q = 2
            compare root: (2 == 2)
            looks good - move left

            - move right

        Step n:
            p = 3, q = 3
            compare root: (3 == 3)
            looks good - check ahead and return True

        return True
        '''
