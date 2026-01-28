class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        m * n 2D grid

        1 - land
        0 - water
        
        1. iterate through the cell
        2. found 1 - increament counter
        3. dfs to mark visited as 0
        4. repeat

        Input: grid = 
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        
        star (0,0), find "1" -> island = 1
        dfs to check connected 1s and mark them as '0'
        
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"]

        island_counter = 1
        '''
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(row, col):
            if(row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0'):
                return

            grid[row][col] = '0'

            dfs(row + 1, col) #down
            dfs(row - 1, col) #up
            dfs(row, col + 1) #right
            dfs(row, col - 1) #left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count

        '''
        Input:
            m * n 
            '1' - land
            '0' - water
            grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]

        Output:
            Num(islands)
            Result: 1

        1. Iterate through the grid
            - check eack cell
        2. When we reach 1 
            - it's an island
            - found '1' at (0, 0)
        3. Increment counter
            - if island found



        Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
        Output: 1

        (0,0): land('1')
        --> island = 1

        '''
