# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            current_diameter = left_height + right_height

            max_diameter = max(max_diameter, current_diameter)

            return 1 + max(left_height, right_height)

        dfs(root)

        return max_diameter

        '''
        Given root of a binary tree
        Return length of the diameter of the tree

        Post order traversal


        Input: root = [1,2,3,4,5]
        Output: 3

        [1,2,3,4,5]

        dfs(1)
            dfs(2)
                dfs(4)

        '''
        self.max_diameter = 0

        def get_depth(node):
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            current_diameter = left_depth + right_depth

            self.max_diameter = max(self.max_diameter, current_diameter)

            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return self.max_diameter
