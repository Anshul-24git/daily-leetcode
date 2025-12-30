class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        '''
        m * n matrix
            sorted asc
            1st next row > last prev row

        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

        Binary search
            Since the whole matrix is a sorted matrix, it acts as a 1D array
            [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            [1,3,5,7,10,11,16,20,23,30,34,60]
        '''
        
