# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            depth += 1

        return depth
        '''
        Given root of BT

        Return max depth

        Max depth : number of nodes along the longest path

        Input: root = [3,9,20,null,null,15,7]
        Output: 3

        3,9,20,null,null,15,7

        2 ways : DFS or BFS

        Let's do BFS

            use a queue
                pocess all nodes level by level
            track the depth
                increment the counter for each level we visit
            when queue empty
                return total depth

        3,9,20,null,null,15,7

                     3
                    / \
                   9   20
                      /  \
                    15     7

        initially : queue = [3], depth = 0
        Level 1 : 
            process 3, add children 9, 20
            queue = [9,20], depth = 1
        Level 2 : 
            process 9, 20, add children 15, 7
            queue = [15, 7], depth = 2
        Level 3 : 
            process 15, 7, add children -> no children :(
            queue = [], depth = 3
        Result : depth = 3
        '''
        # if not root:
        #     return 0

        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return max(left_depth, right_depth) + 1
