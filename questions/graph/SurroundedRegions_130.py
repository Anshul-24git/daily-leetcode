class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return
            
            board[row][col] = 'T'

            #down up right left
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m-1][col] == 'O':
                dfs(m - 1, col)
        
        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n-1] == 'O':
                dfs(row, n - 1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'

        # # Test the solution
        # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        # print("Before:", board)
        # self.solve(board)
        # print("After: ", board)
        '''
        m * n - matrix
        'X' & 'O'
        Input: board = 
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        DFS on border cells:
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","T","X","X"]
        ]
        Capture remaining 'O' -> 'X'
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","T","X","X"]
        ]
        Restore 'T' -> 'O'
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        Complexities:
        Time : O(m * n)
        Space : O(m * n)
        '''
