"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# from typing import Optional
# from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}

        def dfs(node):
            if node in cloned:
                return cloned[node]

            clone = Node(node.val)
            cloned[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)

        # cloned = {}

        # queue = deque([node])

        # cloned[node] = Node(node.val)

        # while queue:
        #     current = queue.popleft()

        #     for neighbor in current.neighbors:
        #         if neighbor not in cloned:
        #             cloned[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)

        #         cloned[current].neighbors.append(cloned[neighbor])

        # return cloned[node]

        '''
        Input: adjList = [
            [2,4],
            [1,3],
            [2,4],
            [1,3]]

        Output: [[2,4],
                 [1,3],
                 [2,4],
                 [1,3]]

         1-----2
         |     |
         4-----3    

         Start


         1. store the original -> cloned nodes (to avoide dups)
         2. use bfs; level by level
         3. create a clone
            - on first node occurance
         4. link the neighbors

        '''        
