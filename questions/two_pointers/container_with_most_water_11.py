class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            
            current_height = min(height[left], height[right])
            
            area = current_height * width

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


        '''
        Given:
            i/p array (height) of len(n)
            n vertical lines
            (i, 0) and (i, height[i])
            area : length * height
        o/p:
            max amount of water

        Brute force:
            Compare all the elements with each other and return max

        Optimized:

            1. Start at extreme ends
            2. Move the shorter pointer
            3. We'll explore all possible scenarios, and return the max area

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49

        [1,8,6,2,5,4,8,3,7]
         0 1 2 3 4 5 6 7 8
        
        Step 1 : 
            left[0] = 1, right[8] = 7 => 1 * 8 = 8
        Step 2 :
            left[1] = 8, right[8] = 7 =>  7 * 7 = 49 : looks promising
        We'll simply continue till we find the left value to be greater than the right
        '''
