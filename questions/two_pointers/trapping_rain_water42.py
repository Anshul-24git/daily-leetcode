class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1

        left_max, right_max = 0, 0

        trapped_water = 0

        while left < right:
            left_max = max(left_max, height[left])

            right_max = max(right_max, height[right])

            if left_max < right_max:
                trapped_water += left_max - height[left]
                left += 1
            else:
                trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

        '''
        Given:
            n non -ve integers
            width of each bar = 1
            Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
            Output: 6
        Sol:
            2 pointers
                left, right = 0, len(height) - 1
            move the lower value pointer
            if we find a curr height < corrosponding max
                add water
        '''
