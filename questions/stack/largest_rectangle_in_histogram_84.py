class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0

        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1

            else:
                top_of_stack = stack.pop()

                area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))

                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()

            area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))

            max_area = max(max_area, area)

        return max_area

        '''
        array of integers heights | width of each bar = 1
        Input : heights = [2,1,5,6,2,3]
        Output: 10 (area of the largest rectangle)

        [2,1,5,6,2,3]

        Stack
            maintain the indices of bars in our stack

        Stack = []
        [2,1,5,6,2,3]
        i = 0, h = 2 -> push 0 => Stack = [0]
        i = 1, h = 1, 1 < 2 -> pop 0, area = 2*1, max_area = 2 -> push 1 => Stack = [1]
        i = 2, h = 5, 5 > 1 -> push 2 => Stack = [1,2]
        i = 3, h = 6, 6 > 5 -> push 3 => Stack = [1,2,3]
        i = 4, h = 2, 2 < 6 -> pop 3, area = 6*(4-2-1) = 6*1 = 6, max_area = 6
                      2 < 5 -> pop 2, area = 5*(4-1-1) = 10 = max_area
                      2 > 1 -> push 4 => Stack = [1,4]
        i = 5, h = 3, 3 > 2 -> push 5 => Stack = [1,4,5] 
        '''
