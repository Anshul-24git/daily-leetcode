from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0 or k > len(nums):
            return []

        dq = deque()
        result = []

        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        '''
        Input array nums and a sliding window k

        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]

        nums = [1,3,-1,-3,5,3,6,7], k = 3
        i = 0, 
        '''
