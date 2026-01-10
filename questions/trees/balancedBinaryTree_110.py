# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0

            left_balanced, left_height = dfs(node.left)

            if not left_balanced:
                return False, -1

            right_balanced, right_height = dfs(node.right)

            if not right_balanced:
                return False, -1

            is_current_balanced = abs(left_height - right_height) <= 1
        
            current_height = max(left_height, right_height) + 1
        
            return is_current_balanced, current_height
    
        balanced, _ = dfs(root)
        return balanced 
        '''
        BT
        determine if it is height balanced

        Input: root = [3,9,20,null,null,15,7]
        Output: true

        DFS : post order

        [3,9,20,null,null,15,7]

                    3
                  /   \
                 9    20
                     /  \
                    15   7
        '''
        # def check_height(node):
        #     if not node:
        #         return 0, True

        #     left_height, left_balanced = check_height(node.left)

        #     if not left_balanced:
        #         return 0, False

        #     right_height, right_balanced = check_height(node.right)

        #     if not right_balanced:
        #         return 0, False

        #     is_current_balanced = abs(left_height - right_height) <= 1

        #     current_height = 1 + max(left_height, right_height)
        #     return current_height, is_current_balanced

        # _, is_tree_balanced = check_height(root)
        # return is_tree_balanced
        

'''
    3
   / \
  9  20
     / \
    15  7      

    

'''
